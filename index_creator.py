import psycopg2

# Use "postgres" as the default database for administrative tasks
connection_string = "postgresql://admin:Batman1@localhost:5432/postgres"
db_name = "vector_db_mapfre_g1"

# Establish the connection
conn = psycopg2.connect(connection_string)
conn.autocommit = True

# Drop and create the database
with conn.cursor() as c:
    c.execute(f"DROP DATABASE IF EXISTS {db_name}")
    c.execute(f"CREATE DATABASE {db_name}")

conn.close()
print(f"Database '{db_name}' has been recreated successfully.")


