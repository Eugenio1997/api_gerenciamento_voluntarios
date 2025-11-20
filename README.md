# 🧩 API de Gerenciamento de Voluntários

API desenvolvida como parte do **desafio técnico backend júnior da FrontEnd Fusion**, cujo objetivo é implementar um sistema simples de gerenciamento de voluntários usando **FastAPI** e **Poetry**, atendendo aos requisitos especificados no repositório oficial do desafio.

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

- **Python 3.13+**
- **FastAPI** (framework principal)
- **Uvicorn** (servidor ASGI)
- **Poetry** (gerenciamento de dependências e ambiente virtual)
- **Pydantic** (modelagem e validação de dados)

---

## 🚀 Requisitos Técnicos

### 1. Estrutura da API

#### 🔗 Endpoints obrigatórios:

```txt
POST    /voluntarios        - Cadastrar novo voluntário
GET     /voluntarios        - Listar voluntários (com filtros)
GET     /voluntarios/{id}   - Buscar voluntário específico
PUT     /voluntarios/{id}   - Atualizar voluntário
DELETE  /voluntarios/{id}   - Excluir voluntário (soft delete)
```

---

## 2. Funcionalidades

- ✅ **Validação de email único** (não permitir duplicatas)  
- 🗓️ **Data de inscrição automática**  
- 🟦 **Soft delete** (marcar como inativo em vez de excluir)  
- 🔍 **Filtros** por status, cargo e disponibilidade  
- ✔️ **Validações básicas nos campos**


## 📁 Estrutura do Projeto

```
api_gerenciamento_voluntarios/
│── .gitignore
│── pyproject.toml
│── poetry.lock
└── app/
    ├── main.py
    ├── __init__.py
    ├── routers/
    │     └── voluntarios.py
    └── models/
          └── voluntario.py
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

---

## 🧱 Modelos e Regras

### Modelo `Voluntario`
```python
class Voluntario(BaseModel):
    nome
    email
    telefone
    cargo_pretendido 
    disponibilidade 
    status 
```

### Observações
- Os dados são armazenados **em memória** (lista simples).
- Não há persistência em banco de dados (não exigido pelo desafio).
- Validações extras podem ser adicionadas (como idade mínima).

---

## 🗂️ Decisões Técnicas

### ✔ Uso de Poetry
O desafio **exige o uso de Poetry**, por isso:

- `pyproject.toml` define as dependências do projeto
- `poetry.lock` fixa as versões exatas

### ✔ Organização Modular
A API foi dividida em:

- Rotas (`routers`)
- Modelos (`models`)
- Arquivo principal (`main.py`)

Facilitando manutenção e futuras expansões.

### ✔ Documentação Automática
FastAPI automaticamente expõe a UI Swagger e Redoc, atendendo ao requisito de clareza e testabilidade.

---

## 👨‍💻 Autor

**Eugenio Lopes Fernandes Lima**  
GitHub: https://github.com/Eugenio1997  

---

## 📜 Licença
Este projeto está sob a licença MIT.
