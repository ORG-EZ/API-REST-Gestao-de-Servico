from dotenv import load_dotenv
import os

# Carrega o .env de forma explícita
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

# Variáveis
DEBUG = os.getenv("DEBUG")
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

# Validação básica
if DEBUG is None or DATABASE_URL is None or SECRET_KEY is None:
    raise ValueError("⚠️ Variáveis de ambiente não configuradas! Copie o .env.example para .env")
