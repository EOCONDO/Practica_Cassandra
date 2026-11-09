# Registro de nombre — Flask + Astra DB

Página con un campo de nombre y un botón **Enviar**. Cada nombre se guarda
en una tabla de Astra DB (DataStax).

## Estructura

```
flask-astra/
├── .env                  # Conexión a Astra DB (ID, región, token)
├── .env.example
├── .gitignore
├── backend/
│   ├── crear_bd.cql      # Crea keyspace y tabla (sin datos)
│   ├── app.py            # Servidor Flask (rutas)
│   ├── db.py             # Conexión a Astra DB
│   ├── test_conexion.py  # Prueba de conexión
│   └── requirements.txt
└── frontend/
    ├── templates/
    │   └── index.html    # Formulario
    └── static/
        └── style.css
```

## 1. Crear la estructura en la nube (una sola vez)

En el portal de Astra: tu base → **CQL Console**. Pega y ejecuta, una sentencia a la vez, el contenido
de `backend/crear_bd.cql`. Crea el keyspace `practica_cassandra` y la tabla `nombres`,
vacía.

Si `CREATE KEYSPACE` da error, usa un keyspace que ya tengas
(`DESCRIBE KEYSPACES;`), reemplaza `practica_cassandra` en el `.cql` y en
`ASTRA_DB_KEYSPACE` del `.env`.

## 2. Completar `.env`

El ID y la región ya están. Falta **ASTRA_DB_APPLICATION_TOKEN**
(portal → *Generate Token*, empieza con `AstraCS:`; se muestra una sola vez).

## 3. Instalar y ejecutar (terminal de VS Code, en la carpeta raíz)

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
python backend/test_conexion.py
python backend/app.py
```

Si PowerShell bloquea la activación, ejecuta una vez:
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

Abre http://127.0.0.1:5000

## Ver los datos guardados

En el CQL Console: `SELECT * FROM practica_cassandra.nombres;`
