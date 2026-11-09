"""Prueba rápida de conexión a Astra DB.

Ejecuta desde la carpeta raíz:  python backend/test_conexion.py
"""
import db

try:
    tabla = db.get_table()
    filas = list(tabla.find({}, limit=5))
    print(f"Conexión correcta. Tabla '{db.KEYSPACE}.{db.TABLE_NAME}' encontrada "
          f"({len(filas)} fila(s) en la muestra).")
except Exception as e:
    print("No se pudo conectar o no existe la tabla (¿ya ejecutaste crear_bd.cql?):")
    print(e)
