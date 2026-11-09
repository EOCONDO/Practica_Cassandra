-- Ejecutar en el CQL Console de Astra DB (portal -> tu base -> CQL Console).
-- Crea SOLO la estructura (keyspace y tabla). No inserta ningún dato.
-- Se usan nombres completos (keyspace.tabla), así no hace falta "USE".
-- Ejecuta las sentencias una por una.

CREATE KEYSPACE IF NOT EXISTS practica_cassandra
  WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 3};

CREATE TABLE IF NOT EXISTS practica_cassandra.nombres (
  id     uuid PRIMARY KEY,
  nombre text,
  creado timestamp
);

-- Verificación (debe devolver 0 filas):
SELECT * FROM practica_cassandra.nombres;
