# 🏋️‍♂️ Workout API - Desafio FastAPI + Docker + PostgreSQL

Este projeto é parte do desafio **"Desenvolvendo sua Primeira API com FastAPI, Python e Docker"** promovido pela [DIO](https://www.dio.me/). A proposta é construir uma API para gerenciamento de **atletas e treinos**, aplicando conceitos como:

- Criação de rotas com **FastAPI**  
- Integração com banco de dados via **SQLAlchemy**  
- Paginação com **fastapi-pagination**  
- Customização de respostas  
- Tratamento de exceções  
- Versionamento com **Git** e publicação no **GitHub**  

---

## 🚀 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [fastapi-pagination](https://pypi.org/project/fastapi-pagination/)
- [Uvicorn](https://www.uvicorn.org/)

---

## 🧰 Instalação e Execução Local

1. **Clone o repositório**:

```bash
git clone https://github.com/seu-usuario/workout_api_clone.git
cd workout_api_clone
```

2. **Crie um ambiente virtual** (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**:

```bash
pip install fastapi sqlalchemy fastapi-pagination uvicorn psycopg2-binary
```

4. **Configure o banco de dados** no arquivo `database.py`:

```python
DATABASE_URL = "postgresql://usuario:senha@localhost:5432/nome_do_banco"
```

5. **Execute a aplicação**:

```bash
uvicorn main:app --reload
```

---

## 🧪 Funcionalidades da API

### 🔍 Buscar atletas com filtros (Query Parameters)

```http
GET /atletas/search?nome=João&cpf=12345678901
```

### 📋 Listar atletas com paginação

```http
GET /atletas?limit=10&offset=0
```

Retorno customizado:
```json
[
  {
    "nome": "João Silva",
    "centro_treinamento": "CT Zona Norte",
    "categoria": "Junior"
  },
  ...
]
```

### ➕ Cadastrar novo atleta

```http
POST /atletas
```

Body JSON:
```json
{
  "nome": "Ana Paula",
  "cpf": "12345678901",
  "centro_treinamento": "CT Sul",
  "categoria": "Sênior"
}
```

### ❗ Tratamento de exceções

Se for enviado um CPF duplicado, a resposta será:

```json
{
  "detail": "Já existe um atleta cadastrado com o cpf: 12345678901"
}
```

Com `status_code: 303`

---

## 📂 Estrutura de Pastas

```
workout_api/
│
├── main.py                # Entrada principal da aplicação
├── models.py              # Modelo de dados Atleta
├── database.py            # Conexão com o banco de dados
├── requirements.txt       # Dependências (opcional)
└── README.md              # Documentação do projeto
```

---

## 💡 Melhorias Sugeridas

- [ ] Criar endpoints para treinos (relacionamento com atletas)
- [ ] Adicionar autenticação com OAuth2 ou JWT
- [ ] Testes automatizados com Pytest
- [ ] Integração contínua com GitHub Actions

---

## 🔗 Links úteis

- 🔗 [Repositório base da DIO](https://github.com/digitalinnovationone/workout_api)
- 🔗 [Documentação do FastAPI](https://fastapi.tiangolo.com/)
- 🔗 [Template no Figma (se houver)](https://figma.com/...)

---

## 👨‍💻 Autor

Desenvolvido por Rosane Dias(https://github.com/RosaneDias)  
Projeto realizado no bootcamp **Santander Python com FastAPI - DIO 2025**