import psycopg2

POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "postgres"
POSTGRES_DB = "postgres"
POSTGRES_HOST = "localhost"
POSTGRES_PORT = 5432


try:
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD
    )
    print("Connected to the database")
except psycopg2.Error as e:
    print(f"Error connecting to the database: {e}")
