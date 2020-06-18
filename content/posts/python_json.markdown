title: Trabalhando com JSON no Python
slug: trabalhando-json-python
category: python
tags: python, json
date: 2019-09-22
modified: 2020-05-10
Summary: Como facilmente manipular um JSON com Python

![Json](/images/json.jpeg)

O JSON (Javascript Object Notation) é o formato mais usado para integração entre sistemas. Toda a linguagem de programação tem sua maneira de manipulá-lo. O Python tem uma biblioteca, chamada json, muito boa e simples de usar para lidar com este tipo de formatação de dados.

A biblioteca **json** tem 4 métodos básicos, tanto para serializar um objeto, quanto para deserializar-lo.

## dump e dumps

Usamos o **dump** e o **dumps** para transformar um objeto do Python (listas, dicionários, tuplas) nos formato **JSON** (serializar). O primeiro serve para jogar um objeto diretamente em um arquivo.

```python
import json
dados = {
    'nome': 'Renato Lelis',
    'profissao': 'Desenvolvedor de sistemas'
}

with open('dados.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4)
```

No exemplo acima eu criei um dicionário com alguns dados e o inseri dentro de um arquivo **.json**. O método **dump** recebe dois argumentos obrigatórios, o objeto que vai ser serializado e o arquivo em que ele vai ser gravado. O resultado:

```json
{
    "nome": "Renato Lelis",
    "profissao": "Desenvolvedor de sistemas"
}
```

O terceiro argumento é número da indentação do **JSON**. Não é obrigatório mas em termos de visualização é um bom argumento para adicionar. Sem ele seu arquivo ficaria assim:

```json
{"nome": "Renato Lelis", "profissao": "Desenvolvedor de sistemas"}
```
E o **dumps** simplesmente transforma o objeto em string (o `s` no final do **dumps** é uma dica) em vez de gravar o objeto dentro de um arquivo.

```python
import json
dados = {
    'nome': 'Renato Lelis',
    'profissao': 'Desenvolvedor de sistemas'
}
dados_json = json.dumps(dados)
print(type(dados_json))
# <class 'str'>
```

Com **dumps** só precisamos dizer qual objeto serializar e ele faz o resto. O argumento **indent** também pode ser utilizado neste método se quiser usá-lo.

## load e loads

Usamos o **load** para fazer o oposto do **dump**, ou seja, deserializar o **JSON** em um objeto do Python.

```python
import json

with open('dados.json', 'r') as json_file:
    dados = json.load(json_file)

print(dados)
print(type(dados))
# {'nome': 'Renato Lelis', 'profissao': 'Desenvolvedor de sistemas'}
# <class 'dict'>
```

Lendo o arquivo que criamos na seção anterior, o método **load** só precisa de um argumento, o arquivo que contém o **JSON**.

E o método **loads**, assim como o **dumps**, é para lidar com **JSON** em formato de string. No caso do **loads**, transformar uma string em um objeto Python.

```python
import json
dados = '{"nome": "Renato Lelis","profissao": "Desenvolvedor de sistemas"}'
dados_json = json.loads(dados)
print(type(dados_json))
# <class 'dict'>
```

Neste artigo, vimos o quão fácil é de se manipular o **JSON** com a biblioteca padrão do Python.
