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

### 🔹 1. Instalar dependências
```bash
poetry install
```

### 🔹 2. Ativar ambiente virtual
```bash
poetry shell
```

### 🔹 3. Executar servidor FastAPI
```bash
uvicorn app.main:app --reload
```

### 🔹 4. Acessar documentação automática
- Swagger UI → http://127.0.0.1:8000/docs  
- ReDoc → http://127.0.0.1:8000/redoc  

---

## 🛠 Funcionalidades Implementadas

### 🔹 `GET /`
Retorna uma mensagem simples indicando que a API está online.

### 🔹 `GET /voluntarios`
Retorna a lista de voluntários cadastrados.

### 🔹 `POST /voluntarios`
Cadastra um novo voluntário conforme o modelo especificado.

#### Exemplo de Corpo JSON:
```json
{
  "nome": "Ana Souza",
  "email": "ana.souza@fusion.com",
  "telefone": "67 996267123"
}
```

#### Exemplo de Resposta:
```json
{
  "message": "Voluntário cadastrado com sucesso!",
  "data": {
    "nome": "Ana Souza",
    "email": "ana.souza@fusion.com",
    "telefone": "67 996267123"
  }
}
```

---

## 🧱 Modelos e Regras

### Modelo `Voluntario`
```python
class Voluntario(BaseModel):
    nome: str
    email: str
    telefone: str
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

## 📌 Próximos Passos (Melhorias Futuras)

- Persistência em banco de dados (SQLite/PostgreSQL)
- Camada de serviços (separando regras de negócio)
- Camada de repositório (abstraindo acesso a dados)
- Testes unitários com `pytest`
- Deploy (Render, Railway, EC2 ou Docker)
- Tratamento de erros customizado com `ExceptionHandlers`

---

## 👨‍💻 Autor

**Eugenio Lopes Fernandes Lima**  
GitHub: https://github.com/Eugenio1997  

---

## 📜 Licença
Este projeto está sob a licença MIT.
