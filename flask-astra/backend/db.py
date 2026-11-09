"""Conexión a Astra DB. Lee los datos del archivo .env de la carpeta raíz."""
import os
from pathlib import Path

from astrapy import DataAPIClient
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

DB_ID = os.getenv("ASTRA_DB_ID")
REGION = os.getenv("ASTRA_DB_REGION")
ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE") or "practica_cassandra"
TABLE_NAME = os.getenv("ASTRA_TABLE") or "nombres"

_table = None


def _get_database(client):
    if not TOKEN:
        raise RuntimeError("Falta ASTRA_DB_APPLICATION_TOKEN en el archivo .env")

    # 1) Endpoint completo
    if ENDPOINT:
        return client.get_database(ENDPOINT, keyspace=KEYSPACE)

    # 2) ID + región -> se arma el endpoint
    if DB_ID and REGION:
        endpoint = f"https://{DB_ID}-{REGION}.apps.astra.datastax.com"
        return client.get_database(endpoint, keyspace=KEYSPACE)

    raise RuntimeError("Completa ASTRA_DB_ID y ASTRA_DB_REGION en el archivo .env")


def get_table():
    """Conecta la primera vez y reutiliza la conexión después.

    La tabla se crea antes con backend/crear_bd.cql (no se crea desde Python).
    """
    global _table
    if _table is not None:
        return _table

    client = DataAPIClient(TOKEN)
    db = _get_database(client)
    _table = db.get_table(TABLE_NAME)
    return _table
