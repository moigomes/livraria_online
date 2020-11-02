# livraria_online

Livraria online é uma API REST desenvolvida em Python3.6 utilizando o Framework [Django REST framework](https://www.django-rest-framework.org/).
Possibilita cadastrar clientes, livros e realizar empréstimos.




#### 1 -  Clonar projeto:
```sh
git clone https://github.com/moigomes/livraria_online.git
```

#### 2 - Criar Ambiente Virtual:
```sh
cd livraria_online
python3 -m venv env
source env/bin/activate
```

#### 3 - Instalar dependências:
```sh
pip install -r requirements.txt
```


#### 4 - Realizar migrações(database):
```sh
python manage.py makemigrations
python manage.py migrate
```


#### 5 - Run API:
```sh
python manage.py runserver
```

#

## Uso:

#### Cadastrando livros:
POST /livros/
```sh
{
    "codigo": "string",
    "titulo": "string",
    "autor": "string",
    "ano_lancamento": int,
    "valor_emprestimo": decimal
}
```
#
#### Cadastrando clientes:
POST /clientes/
```sh
{
   "nome": "string",
   "telefone": "string"
}
```
#
#### Realizando empréstimo:
POST /emprestimos/
```sh
{
    "livro": int,
    "cliente": int,
    "data_retirada": "string"
}
```
#
#### Listagem de livros emprestados por Cliente:
GET /clientes/{cliente_id}/livros

#
#### Listagem de todos livros:
GET /livros


#
#### Testes:
```sh
python manage.py test
```




