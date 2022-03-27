

# Criação de um app de relatório de vendas.

## Link do projeto e da api em produção.

[App em produção]

## Ferramentas

- Django
- Postgres
- Docker
- Heroku

## Roda o projeto localmente:

1. Clone o repositório.
2. Entre na pasta.
3. Crie um ambiente de desenvolvimento com python 3.9.
4. Ative o ambiente.
5. Instale as dependências.
6. Crie um arquivo .env
7. Rode as migrações
8. Rode o projeto
9. Acesse o link

```
- git clone git@github.com:ffabiorj/cadastro_empresa.git
- cd cadastro_empresa
- python3 -m venv .venv
- source .venv/bin/activate
- pip install -r requirements-dev.txt
- python contrib/env_gen.py
- python manage.py migrate
- python manage.py runserver
- http://127.0.0.1:8000/
```



### Rodar os testes

```

pytest

```

### Links para as ferramentas utilizadas

[Django](https://docs.djangoproject.com/)

[Postgres](https://www.postgresql.org/)

[Heroku](https://www.heroku.com/)

[Docker](https://www.docker.com/)
