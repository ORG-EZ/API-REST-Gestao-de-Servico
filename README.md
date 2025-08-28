# API REST de Gestão de Ordens de Serviço



API REST desenvolvida em **Python** com **FastAPI** para gerenciar **ordens de serviço**.  
Permite **criação, listagem, atualização e exclusão** de registros, com **validação automática** de dados usando **Pydantic** e integração com **PostgreSQL** via **SQLAlchemy**.

---

## **Stacks Utilizadas**


````markdown
- Linguagem: Python 3.12+
- Framework Web: FastAPI
- Banco de Dados: PostgreSQL (via Docker)
- ORM: SQLAlchemy
- Validação: Pydantic
- Testes: pytest
- Gerenciamento de ambiente: venv
- Documentação: Swagger UI embutida

````
---

## **Configuração do Projeto**

### **1. Clonar o repositório**

```bash
git clone https://github.com/ORG-EZ/API-REST-Gestao-de-Servico.git
cd API-REST-Gestao-de-Servico
````


---

### **2. Versionamento do .env

Não versionar o .env real com senhas e chaves secretas.
Mantenha apenas o .env.example no Git. Cada pessoa copia para .env e ajusta suas credenciais locais:

```bash
cp backend/app/.env.example backend/app/.env
```

---


### **3. Criar o ambiente virtual (venv) e instalar dependências**

```bash
python3 -m venv venv
source venv/bin/activate      # Linux / Mac
# venv\Scripts\activate       # Windows
pip install -r backend/requirements.txt
```

---

### **4. Banco de dados**

```bash
docker compose up -d

```

---

* **Host:** `localhost`
* **Porta:** `5432`
* **Usuário:** definido no `docker-compose.yml`
* **Senha:** definida no `docker-compose.yml`
* **Banco:** `ordens_db`

---

### **6. Rodar o servidor FastAPI**

No diretório `backend`:

```bash
uvicorn app.main:app --reload
```

O servidor subirá em:

* **API Base URL:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

### **7. Rodar os testes com pytest**

Certifique-se de estar na raiz do backend (backend/) e com o venv ativo:

```bash
cd backend
pytest
```
Observação:

Arquivos de teste devem começar com test_ (ex: test_ordens.py)

Funções de teste devem começar com test_ (ex: def test_criar_ordem():)

O pytest procura automaticamente por todos os arquivos/funções com esse padrão.

---

## **Estrutura do Projeto**

```bash
API-REST-Gestao-de-Servico/
├── backend/
│   ├── app/
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   ├── models/
│   │   │   ├── ordem.py
│   │   ├── routers/
│   │   │   ├── ordens.py
│   │   ├── schemas/
│   │   │   ├── ordem.py
│   │   ├── tests/
│   │   │   ├── test_ordens.py
│   │   ├── __init__.py
│   │   ├── .env
│   │   ├── main.py
│   ├── Dockerfile
│   ├── requirements.txt
├── docker-compose.yml
├── frontend/
├── README.md
└── .gitignore
```

---

## **Documentação Automática**

O FastAPI gera automaticamente a documentação interativa:

* **Swagger:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## **Comandos principais**

| **Comando**                       | **Descrição**                    |
| --------------------------------- | -------------------------------- |
| `python3 -m venv venv`            | Cria o ambiente virtual          |
| `source venv/bin/activate`        | Ativa o ambiente (Linux/Mac)     |
| `venv\Scripts\activate`           | Ativa o ambiente (Windows)       |
| `pip install -r requirements.txt` | Instala as dependências          |
| `docker-compose up -d`            | Sobe o banco de dados PostgreSQL |
| `uvicorn app.main:app --reload`   | Roda o servidor FastAPI          |
| `pytest`                          | Executa os testes unitários      |

---

## **Licença**

Este projeto está sob a licença **MIT**.
Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.


