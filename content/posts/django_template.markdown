title: Entendendo o sistema de templates do Django
slug: django-template
category: web
tags: django
authors: Renato Lelis
date: 2019-06-23
modified: 2020-05-10
Summary: Entendendo como a engine de templates do Django funciona

![Forma de bolo](/images/forma.jpeg)

Sendo considerado um framework full stack, o Django possui funcionalidades que abrangem desde da modelagem de dados com sua própria ORM até o front-end, com seu sistema completo de templates. Neste artigo vamos discutir como este sistema funciona, suas funcionalidades básicas e algumas mais avançadas.

O sistema de templates do Django existe basicamente exibir informações vindo das `views` no front-end da aplicação e formatar páginas(os templates) com código escritos em python. O Django dispõe de três tipos tags especiais para fazer esta formatação.

A primeira delas é a variável de template. Ela é representada pelas chaves duplas `{{ }}`. Esta tag possibilita simplesmente exibir dados de uma variável vindos da view.

```html
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>{{ usuario.nome }}</p>
    <p>{{ usuario.email }}</p>
    <p>{{ usuario.data_de_nascimento }}</p>
  </body>
</html>
```

É uma funcionalidade bem básica e o que chama a atenção é a simplicidade dela. É fácil de ler e fácil de identificar do que se trata.

A próxima tag é o filter, funcionando como uma extensão da anterior, representado pelas chaves duplas, contendo um pipe no meio `{{ | }}`. Conhecida como filtro, ela adiciona uma formatação à informação que vai ser renderizada.

```html
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>{{ usuario.nome }}</p>
    <p>{{ usuario.email }}</p>
    <p>{{ usuario.data_de_nascimento | date:'d/m/Y'}}</p>
  </body>
</html>
```

No exemplo acima, o filtro é aplicado a data de nascimento do usuário. O filtro funciona da seguinte forma: entre as chaves duplas `{{}}` é passada a informação a ser renderizada e, separado por um pipe, o tipo de filtro a ser aplicado nessa informação. Você pode conferir os tipos de filter e como aplicá-los na [documentação](https://docs.djangoproject.com/pt-br/3.0/ref/templates/builtins/#filter) oficial do Django.

Por último mas não menos importante vem as `expressions`. Representadas como `{%%}`, elas nos dão a possibilidade de executar comandos do Python dentro de nossos templates.

```html
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    {% for usuario in usuarios %}
      <p>{{ usuario.nome }}</p>

      {% if usuario.email %}
        <p>{{ usuario.email }}</p>
      {% else %}
        <p>{{ E-mail não cadastrado }}</p>
      {% endif %}

      <p>{{ usuario.data_de_nascimento | date:'d/m/Y'}}</p>
    {% endfor %}
  </body>
</html>
```

Nesse exemplo vemos a aplicação de código Python nos templates do Django. Temos um `for`, onde a lista de usuários é iterada, e um `if\else` simples checando se existe um email cadastrado para aquele usuário. Note que todas as `expressions`, com exceção de algumas, terminam com um `end`.

## Tags avançadas

O Django disponibiliza algumas `expressions` próprias que, não servem para escrever código em Python, porém auxiliam no desenvolvimento de funcionalidades do template e também ajudam no reuso de código. Dessas `expressions`, as mais usadas são o `extends`, o `url` e o `static`.

O `extends` faz com que se crie um padrão de layout nos templates, onde um template pai carrega toda a formatação básica das páginas deixa um espaço para os templates filhos serem carregados.

```html
<!DOCTYPE html>
 <html>
  <head>
    <title>{% block title %} Página base {% endblock title %}</title>
  </head>
  <body>
    {% block content %}
    {% endblock content %}
  </body>
</html>
```

A tag `block` é usada para delimitar o espaço onde o template filho vai ser renderizado.

```html

{% extends 'base.html' %}
{% block title%} Lista de usuários {% endblock title %}
{% block content %}
  {% for usuario in usuarios %}
    <p>{{ usuario.nome }}</p>

    {% if usuario.email %}
      <p>{{ usuario.email }}</p>
    {% else %}
      <p>{{ E-mail não cadastrado }}</p>
    {% endif %}

     <p>{{ usuario.data_de_nascimento | date:'d/m/Y'}}</p>
  {% endfor %}
{% endblock content %}
```

O `extends` é usado para dizer ao Django qual é o template pai e o `block` nesse escopo é para dizer quais informações vão ser renderizadas nos espaços pré-determinados.

No template pai, note que existe uma informação no bloco `title`. Se, no template filho, alguma informação for passada nesse bloco, a informação do template filho prevalece, sobrescrevendo a do template pai.

No final, o html renderizado é o seguinte:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Lista de usuários</title>
  </head>
<body>
  {% for usuario in usuarios %}
    <p>{{ usuario.nome }}</p>

    {% if usuario.email %}
      <p>{{ usuario.email }}</p>
    {% else %}
      <p>{{ E-mail não cadastrado }}</p>
    {% endif %}

    <p>{{ usuario.data_de_nascimento | date:'d/m/Y'}}</p>
    {% endfor %}
  </body>
</html>
```

O oportunidade de reuso de código aqui é grande e é uma coisa comum em projetos Django.

A tag `url` renderizar a url de uma função da `view`, mapeada por um namespace.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Lista de usuários</title>
   </head>
  <body>
    {% for usuario in usuarios %}
      <p>{{ usuario.nome }}</p>

      {% if usuario.email %}
        <p>{{ usuario.email }}</p>
      {% else %}
        <p>{{ E-mail não cadastrado }}</p>
      {% endif %}

      <p>{{ usuario.data_de_nascimento | date:'d/m/Y'}}</p>
      <a href="{% url 'usuarios:usuario-detalhe' pk=usuario.id %}">
    {% endfor %}
  </body>
</html>
```

O primeiro argumento é o namespace da função e os seguintes são os argumentos que serão passados para a função. No exemplo acima, a url que irá ser renderizada é o da função de detalhe do usuário e o argumento passado é o id do usuário para a função realizar a consulta.

Outra tag bastante utilizada é tag `static`. Ela é usada para carregar recursos estáticos da aplicação, como imagens, javascript e css.

```html
{% load static %}
<!DOCTYPE html>
<html>
  <head>
    <title>{% block title %} Página base {% endblock title %}</title>
    <link rel='stylesheet' href='{% static usuario/css/main.css %}'>
   </head>
  <body>
    {% block content %}
    {% endblock content %}
    <script src='{% static usuario/js/main.js %}'>
  </body>
</html>
```

Esta tag serve para renderizar o caminho absoluto dos recursos, utilizando o namespace. Para ser usada, a tag `static` deve ser carregada para o template usando a tag `load`, colocada bem no início do documento html.

Geralmente, os recursos estático são carregados dentro do template pai, aumentando ainda mais o reuso. Mas nada impede desses recursos serem importados nos templates filho.

Neste artigo falei um pouco sobre o sistema de templates do Django e suas funcionalidades.

O sistema de templates do Django foi pensado, assim como o próprio Python, para ter um código legível e simples de ser implementado e de dar manutenção. A documentação oficial do sistema de templates do Django você pode conferir [aqui](https://docs.djangoproject.com/pt-br/3.0/ref/templates/).

Uma coisa que falei algumas vezes durante este artigo foi o uso de namespace. Ele é muito importante no desenvolvimento do Django. Irei detalhar esta importância em outro futuro artigo.
