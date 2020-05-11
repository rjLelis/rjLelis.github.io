title: Entendendo a arquitetura do Django
slug: entendendo-arquitetura-django
category: web
tags: django
authors: Renato Lelis
date: 2019-06-15
modified: 2020-05-10
Summary: Entendendo a arquitetura MTV

![Arquitetura](/images/arquitetura.png)

No início do desenvolvimento de um sistema, é importante que o desenho da arquitetura esteja bem definida e que todos os desenvolvedores sigam ela a risca (bom item para o peer review). No desenho da arquitetura, é levado em consideração performance, escalabilidade e manutenção.

A muitas arquitetura usadas por padrão hoje em dia e alguns frameworks são construídos para seguir elas. No caso do Django o modelo adotado é a arquitetura MTV.

![Desenho da arquitetura MTV](/images/mtv.png)

Dividida em três camadas, a arquitetura MTV consiste na camada **M**odel, **T**emplate e da camada **V**iew.

A camada `Model` é responsável pela interface com o banco de dados. É onde o Django fornece sua ORM para a modelagem de dados.

```python
from django.db import models

class Usuario(models.Model):
  nome = models.CharField(max_length=200)
  email = models.EmailField(max_length=100)
  telefone = models.CharField(max_length=9)
  data_de_nascimento = models.DateField()
```

**obs: O Django já fornece uma tabela padrão de usuários, o código acima é só um exemplo da ORM.**

O Model vai servir como base da aplicação, onde vai ser extraído e persistido informação da aplicação, fazendo conexão (mas não necessariamente) com a camada View.

A próxima camada é a de `Template`. Nela é onde os dados vão ser apresentados no browser. Esta camada consiste basicamente de arquivos .html com algumas funcionalidades que o Django fornece para apresentar os dados vindos da camada View. Essas funcionalidades são expressões, envolvidas em chaves.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Título da página</title>
  </head>
  <body>
    {% for usuario in usuarios %}
      <p>{{ usuario.nome }}</p>
      <p>{{ usuario.email }}</p>
      <p>{{ usuario.telefone }}</p>
      <p>{{ usuario.data_de_nascimento | date:'d/m/Y' }}</p>
    {% endfor %}
  </body>
</html>
```

Existem três tipos de expressões. A primeira delas é o `{% %}`, que permite executar comandos do python, como o for eachs e o ifs, e outras funcionalidades do próprio sistema de templates do Django.

A outra expressão é o `{{ }}`, ele é usado para acessar variáveis e mostrá-las na tela. Simples assim.

E a última expressão é uma variação da anterior, que é simplesmente um filtro representado pelo pipe. No exemplo mostrado é aplicado um filtro de data na variável **usuario.data_de_nascimento**. Há diversos filtros disponíveis, você pode conferir mais delas [aqui](https://docs.djangoproject.com/pt-br/3.0/ref/templates/builtins/).

E por fim vem a camada de `View`. Nela é onde as informações dos templates são tratadas. Existem dois tipos de views, as baseadas em função e as baseadas em classes.

As view baseadas em função(FBV) são funções normais do python, recebem um parâmetro obrigatório, o request, tem sua lógica dentro de si e retornam as informações necessárias para renderizar no template.

```python
from django.shortcuts import render
from .models import Usuario

def list_usuarios(request):
  context = {
    'usuarios': Usuario.objects.all()
  }

  return render(request, 'usuario/list_usuarios.html', context=context)
```

Nesta função é criado um dicionário `context`, nela irá conter as informações para ser passadas para o template. Dentro do `context` é feita uma consulta para retornar todos os usuários e por fim, na função render, é passado o próprio request, o template que vai ser direcionado as informações do `context` e o `context` em si.

E as views baseadas em classes(CBV) são classes que o Django genericas que abstraem a lógica das FBVs.

```python
from django.views.generics import ListView
from .models import Usuario


class UsuarioListView(ListView):
  model = Usuario
  template_name = 'usuario/list_usuarios.html'
  object_context_name = 'usuarios'
```

Com CBVs você sobre precisa dizer o model e o template que o Django faz a mágica.

Particularmente, eu prefiro as FBVs porque dão mais liberdade para fazer as regras de negócio mas, se não for uma lógica muito complexa, uma CBVs não vai fazer mal.

Nesse post, vimos a importância de uma arquitetura bem estruturada, o model de arquitetura que o Django adota e detalhamos as responsabilidades de suas camadas.
