import os
from dotenv import load_dotenv
import urllib

# Cargar variables de entorno
load_dotenv()

# Obtener variables de entorno
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
DATABASE_SERVER = os.getenv('DATABASE_SERVER', '127.0.0.1')
DATABASE_PORT = os.getenv('DATABASE_PORT', '1433')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'StoreDB')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'sa')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'Password1*')

# Construir la cadena de conexión
params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={DATABASE_SERVER},{DATABASE_PORT};"
    f"DATABASE={DATABASE_NAME};"
    f"UID={DATABASE_USERNAME};"
    f"PWD={DATABASE_PASSWORD};"
    f"Persist Security Info=yes;"
    f"MultipleActiveResultSets=yes;"
    f"TrustServerCertificate=yes;"
)

DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"