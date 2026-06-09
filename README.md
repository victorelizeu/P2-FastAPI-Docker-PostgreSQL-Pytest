# 📦 Gerenciador de Ativos 3D - API RESTful

Projeto de Backend desenvolvido como requisito de avaliação (P2) para o curso de Engenharia de Software da Univassouras.

Esta é uma API RESTful completa para o gerenciamento de um catálogo de modelos e ativos 3D. A aplicação permite cadastrar, listar, atualizar e deletar informações sobre malhas, personagens e cenários, persistindo os dados de forma segura em um banco de dados relacional.

---

# 🚀 Tecnologias Utilizadas

A arquitetura do projeto foi construída utilizando as seguintes tecnologias e boas práticas de mercado:

- **Python 3.11** — Linguagem principal do projeto.
- **FastAPI** — Framework web assíncrono e de alta performance para construção da API.
- **PostgreSQL** — Banco de dados relacional.
- **SQLAlchemy 2.0** — ORM (Object-Relational Mapping) para comunicação com o banco de dados.
- **Pydantic** — Validação e serialização de dados (Schemas).
- **Docker & Docker Compose** — Containerização e orquestração de serviços.
- **Pytest** — Framework para testes automatizados da aplicação.

---

# ⚙️ Como Executar o Projeto

Como o projeto é 100% containerizado, você não precisa instalar o Python ou o PostgreSQL diretamente na sua máquina, apenas o Docker.

## Pré-requisitos

- Docker
- Docker Compose

## Passo a Passo Inicial

1. Clone este repositório para a sua máquina local.
2. Pelo terminal, navegue até a pasta raiz do projeto.
3. Suba os containers em segundo plano executando o comando:

```bash
docker-compose up -d --build
```

4. Aguarde alguns segundos para que o banco de dados inicialize e o FastAPI crie as tabelas automaticamente.
5. O servidor estará rodando na porta **8080**.

---

# 📖 Documentação Interativa (Swagger)

O FastAPI gera a documentação da API automaticamente. Com os containers rodando, acesse no navegador:

```text
http://localhost:8080/docs
```

Lá você encontrará a interface interativa do Swagger UI, onde é possível visualizar o formato esperado dos JSONs e testar todos os endpoints de CRUD (**Create, Read, Update e Delete**) diretamente pelo navegador.

---

# 🔗 Endpoints Principais

| Método   | Endpoint             | Descrição                                   |
| -------- | -------------------- | ------------------------------------------- |
| `GET`    | `/`                  | Health Check (verifica se a API está no ar) |
| `POST`   | `/assets/`           | Cadastra um novo ativo 3D                   |
| `GET`    | `/assets/`           | Lista todos os ativos 3D cadastrados        |
| `GET`    | `/assets/{asset_id}` | Busca um ativo 3D específico pelo ID        |
| `PUT`    | `/assets/{asset_id}` | Atualiza os dados de um ativo existente     |
| `DELETE` | `/assets/{asset_id}` | Exclui um ativo do banco de dados           |

---

# 🧪 Como Rodar os Testes Automatizados

O projeto conta com uma suíte de testes construída com **Pytest** e o **TestClient do FastAPI** para garantir a integridade das rotas.

Para executar os testes com a aplicação rodando, utilize o seguinte comando:

```bash
docker-compose exec fastapi pytest
```

### Exemplo de Saída

```text
=============================================== test session starts ================================================
platform linux -- Python 3.11.15, pytest-9.0.3, pluggy-1.6.0
rootdir: /app
plugins: anyio-4.13.0
collected 6 items

test_main.py ......                                                                                          [100%]

=========================================== 6 passed, 1 warning in 0.96s ===========================================
```

✅ Todos os testes foram executados com sucesso.

---

# 👨‍💻 Autor

**João Victor Elizeu Silva**

Graduação em Engenharia de Software
