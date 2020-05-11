title: Flask vs Django — Rotas
slug: flask-django-rotas
category: web
tags: django, flask
date: 2019-06-11
modified: 2020-05-10
Summary: Comparando como lidar com rotas nos dois frameworks mais famosos do Python

![Rotas](/images/flask_django_rotas.jpeg)

Todo framework web (ou quase todos, não cheguei a trabalhar com todos) tem seu meio de fazer rotas entre suas função e as requisições do que vem do cliente. Nessas rotas também é possível configurar o método HTTP, onde uma rota `/user` com o método **GET** irá gerar um resultado diferente da rota `/user` com o método **DELETE**.

No modelo de arquitetura **REST**, os métodos HTTP têm semântica. Nele é recomendado que o método **GET** seja usado para consultas, o método **POST** para inserir informações, o **PUT** para atualizar e o **DELETE** para deletar. O **REST** determina outras boas práticas mas elas não vem ao caso agora.

No Django, as rotas são criadas num arquivo chamado urls.py, numa lista chamada `urlpatterns`.

```python
from django.urls import path
from . import views

namespace = 'usuario'

urlpatterns = [
  path('user/', views.list_users, name='list-users'),
  path('user/<int:pk>', views.user_details, name='user-detail'),
]
```

Essa lista recebe a função `path()`, onde é passado a rota e qual a função do módulo **views.py** irá ser chamada.

No caso do Flask, um decorator é usado para criar as rotas.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/user')
def list_users():
    # retorna uma lista de usuários

@app.route('/user/<int:id>')
def user_details(id):
    # retorna detalhes de um usuário
```

É o mesmo princípio usado no Django, cada função recebe um decorator, `@app.routes`, onde é passado sua rota.

A diferença aqui, é que o Django faz isso em arquivos separados e o Flask consegue fazer em um arquivo só (na verdade o Flask permite criar uma aplicação em um único arquivo se você quiser).

Outra grande diferença é o segundo argumento no decorator do Flask. Nele nós passamos uma lista de métodos HTTP e quando essa rota for chamada, dependendo do método, uma função diferente é chamada.

```python
@app.route('/user', methods=['GET'])
def list_users():
  # retorna uma lista de usuários


@app.route('/user', methods=['POST'])
def create_user():
  # insere um novo usuário na base
```
No exemplo acima, a rota é a mesma mas os métodos são diferentes, separando as funções que vão ser chamadas.

No Django, a diferenciação de métodos HTTP deve ser feita dentro da função chamada pela rota.

```python
def list_create_user(request):
  if request.method == 'GET':
    # lista os usuários
  elif request.method == 'POST':
    # cria um usuário
```

Com isso, sempre que houver a necessidade de alteração em alguma lógica de inserção ou de busca, a alteração vai acontecer em uma única função. Isso deixa a manutenção do código mais engessada.

Enquanto o Flask oferece mais flexibilidade e simplicidade nas rotas, o Django oferece mais velocidade na prototipagem (class based views for the win!) e uma arquitetura bem definida, embora obrigue o desenvolvedor a usar suas convenções.
