import os
from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context

# Importa tu Base de modelos para que Alembic detecte los modelos
from database import Base
from entitites.author_entity import AuthorEntity
from entitites.book_entity import BookEntity

# Carga la configuración de Alembic
config = context.config

# Configura el logging
fileConfig(config.config_file_name)

# Obtén la metadata de los modelos
target_metadata = Base.metadata

# Configura la URL de conexión desde las variables de entorno o directamente
DATABASE_URL = os.getenv("DATABASE_URL")

# Si DATABASE_URL no está definida, configura la URL aquí directamente:
if not DATABASE_URL:
    DATABASE_SERVER = '127.0.0.1'
    DATABASE_PORT = '1433'
    DATABASE_NAME = 'StoreDB'
    DATABASE_USERNAME = 'sa'
    DATABASE_PASSWORD = 'Password1*'
    
    # Construye la cadena de conexión codificada
    DATABASE_URL = (
        f"mssql+pyodbc:///?odbc_connect="
        f"DRIVER%3D%7BODBC+Driver+17+for+SQL+Server%7D%3B"
        f"SERVER%3D{DATABASE_SERVER}%2C{DATABASE_PORT}%3B"
        f"DATABASE%3D{DATABASE_NAME}%3BUID%3D{DATABASE_USERNAME}%3B"
        f"PWD%3D{DATABASE_PASSWORD}%3B"
        f"Persist+Security+Info%3Dyes%3B"
        f"MultipleActiveResultSets%3Dyes%3B"
        f"TrustServerCertificate%3Dyes%3B"
    )

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_engine(
        DATABASE_URL,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
