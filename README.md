# 🧩 API de Gerenciamento de Voluntários

API desenvolvida como parte do **desafio técnico backend júnior da FrontEnd Fusion**, cujo objetivo é implementar um sistema de gerenciamento de voluntários usando **FastAPI** e **Poetry**, atendendo aos requisitos especificados no repositório oficial do desafio.

---

## 📌 Objetivo do Desafio

O desafio consiste em construir:

- Uma API REST funcional
- Que permita cadastrar, listar, editar e deletar  voluntários
- Utilizando **FastAPI** + **Pydantic**
- E gerenciando dependências com **Poetry**

A solução também deve demonstrar organização, boas práticas e clareza de código.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.12**
- **FastAPI** (framework principal)
- **Uvicorn** (servidor ASGI)
- **Poetry** (gerenciamento de dependências e ambiente virtual)
- **Pydantic** (modelagem e validação de dados)

---

## 🚀 Requisitos Técnicos

### 1. Estrutura da API

#### 🔗 Endpoints disponíveis:

```txt
POST    /voluntarios        - Cadastrar novo voluntário
GET     /voluntarios        - Listar voluntários (com filtros)
GET     /voluntarios/{id}   - Buscar voluntário específico
PUT     /voluntarios/{id}   - Atualizar voluntário
DELETE  /voluntarios/{id}   - Excluir voluntário (soft delete)
```

---

### 2. Funcionalidades

- ✅ **Validação de email único** (não permitir duplicatas)  
- 🗓️ **Data de inscrição automática**  
- 🟦 **Soft delete** (marcar como inativo em vez de excluir)  
- 🔍 **Filtros** por status, cargo e disponibilidade  
- ✔️ **Validações básicas nos campos**

---

## 🧱 Decisões Técnicas
✔ Alias em português nos modelos (Pydantic v2)

Permite manter atributos internos em inglês mas expor nomes em PT-BR.

✔ Soft delete

Nenhum voluntário é removido — apenas marcado como inativo.

✔ Filtros

Implementados usando classe de dependência VolunteerFilters.

✔ Armazenamento em memória

Simula um banco de dados, conforme desafio.

---

## 📁 Estrutura do Projeto

```
app
├── .gitignore
├── __init__.py
├── main.py
├── routers
│   ├── __init__.py
│   └── volunteer_router.py
├── schemas
│   ├── enums.py
│   └── volunteer.py
├── services
│   └── volunteer_service.py
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   └── test_services
│       ├── test_create_volunteer.py
│       └── test_get_volunteer.py
└── utils
    ├── __init__.py
    └── filters.py
```
---

## 🧪 Testes Automatizados

--- poetry run pytest -vv

---

## 📘 Exemplos de Requests & Responses

---

## 🎯 1. Criar voluntário — POST /voluntarios

### 📤 Request
```http
POST /voluntarios
Content-Type: application/json
```

```json
{ 
  "nome": "Mariana Alves",
  "email": "mariana.alves@example.com",
  "telefone": "(11) 98888-7777",
  "funcao_desejada": "desenvolvedor",
  "disponibilidade": "manhã",
  "status": "ativo"
}
```

### 📥 Response — 201 Created
```json
{
  "id": 6,
  "nome": "Mariana Alves",
  "email": "mariana.alves@example.com",
  "telefone": "(11) 98888-7777",
  "funcao_desejada": "developer",
  "disponibilidade": "morning",
  "status": "active",
  "data_registro": "2025-11-20T19:40:10.123Z"
}
```

---

## 🟩 2. Listar voluntários com filtros

### 📤 Request
```http
GET /voluntarios?status=ativo&funcao_desejada=desenvolvedor
```

### 📥 Response — 200 OK
```json
[
  {
    "id": 1,
    "nome": "Maria Silva",
    "email": "maria.silva@example.com",
    "telefone": "(11) 91234-5678",
    "funcao_desejada": "developer",
    "disponibilidade": "morning",
    "status": "active",
    "data_registro": "2025-11-20T18:20:30.550Z"
  }
]
```

---

## 🔎 3. Buscar voluntário por ID

### 📤 Request
```http
GET /voluntarios/1
```

### 📥 Response — 200 OK
```json
{
  "id": 1,
  "nome": "Maria Silva",
  "email": "maria.silva@example.com",
  "telefone": "(11) 91234-5678",
  "funcao_desejada": "desenvolvedor",
  "disponibilidade": "manhã",
  "status": "ativo",
  "data_registro": "2025-11-20T18:20:30.550Z"
}
```

---

## 🛠️ 4. Atualizar voluntário

### 📤 Request
```http
PUT /voluntarios/1
Content-Type: application/json
```

```json
{
  "nome": "Maria Silva",
  "email": "maria.silva@example.com",
  "telefone": "(11) 99999-2222",
  "funcao_desejada": "desenvolvedor",
  "disponibilidade": "tarde",
  "status": "ativo"
}
```

### 📥 Response
```json
{
  "id": 1,
  "nome": "Maria Silva",
  "email": "maria.silva@example.com",
  "telefone": "(11) 99999-2222",
  "funcao_desejada": "developer",
  "disponibilidade": "afternoon",
  "status": "active",
  "data_registro": "2025-11-20T18:20:30.550Z"
}
```

---

## 🗑️ 5. Soft Delete

### 📤 Request
```http
DELETE /voluntarios/1
```

### 📥 Response — 204 No Content

Internamente o status muda para:
```json
{ "status": "inactive" }
```

---

## 📦 Instalação e Execução

### 🔹 1. Pré-requisitos
```bash
# Instale o Poetry se não tiver
curl -sSL https://install.python-poetry.org | python3 -
# ou
pip install poetry
```

### 🔹 2. Criar ambiente + instalar dependências
```bash
poetry install
```

### 🔹 3. Ativar ambiente virtual
```bash
poetry shell
```

### 🔹 4. Executar servidor Uvicorn (servidor ASGI)
```bash
poetry run uvicorn app.main:app --reload
```

### 🔹 5. Acessar documentação automática
- Swagger UI → http://127.0.0.1:8000/docs  
- ReDoc → http://127.0.0.1:8000/redoc  

---

## 🧱 Modelos e Regras

### Modelo `Voluntario`
A API utiliza modelos Pydantic com alias em português.
```python
class Voluntario(BaseModel):
    name: str = Field(..., alias="nome")
    email: EmailStr = Field(..., alias="email")
    phone: str = Field(..., alias="telefone")
    desired_role: str = Field(..., alias="funcao_desejada")
    availability: str = Field(..., alias="disponibilidade")
    status: str = Field(..., alias="status")
    registration_date: datetime = Field(..., alias="data_registro")
```

---

🧱 Decisões Técnicas
✔ Alias em português nos modelos (Pydantic v2)

Permite manter atributos internos em inglês mas expor nomes em PT-BR.

✔ Soft delete

Nenhum voluntário é removido — apenas marcado como inativo.

✔ Filtros

Implementados usando classe de dependência VolunteerFilters.

✔ Armazenamento em memória

Simula um banco de dados, conforme desafio.

---

### ✔ Organização Modular

A API foi organizada em uma estrutura modular, separando responsabilidades de forma clara:

Rotas (routers/)
Contém os endpoints da aplicação, como o volunteer_router.py.

Modelos e Validações (schemas/)
Inclui os modelos Pydantic (volunteer.py) e os enums utilizados pela API (enums.py).

Serviços (services/)
Implementa as regras de negócio e operações da aplicação, como o volunteer_service.py.

Utilidades (utils/)
Inclui funções auxiliares, como filtros usados em operações internas.

Testes Automatizados (tests/)
Estrutura dedicada aos testes com Pytest, contendo:

conftest.py para configuração do ambiente de testes

Testes organizados em submódulos, como test_services/.

Arquivo Principal (main.py)
Ponto de entrada da aplicação FastAPI, responsável por iniciar a API e registrar as rotas.

Essa separação facilita a manutenção, amplia a legibilidade e permite a expansão do projeto de forma organizada e escalável.

### ✔ Documentação Automática
FastAPI automaticamente expõe a UI Swagger e Redoc, atendendo ao requisito de clareza e testabilidade.

---

## 👨‍💻 Autor

**Eugenio Lopes Fernandes Lima**  
GitHub: https://github.com/Eugenio1997  

---

## 📜 Licença
Este projeto está sob a licença MIT.
