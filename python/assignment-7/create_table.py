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

# Creating a database and a table
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")
print("Table created")

# Inserting data into the table
print("Data inserting into the table")
cursor.execute("INSERT INTO users (name, email) VALUES ('John Doe', 'john.doe@example.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Jane Doe', 'jane.doe@example.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Jim Doe', 'jim.doe@example.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Jill Doe', 'jill.doe@example.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Jack Doe', 'jack.doe@example.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Jill Doe', 'jill.doe@example.com')")
print("-"* 100)

# Selecting data from the table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Data selected from the table")
for row in rows:
    print(row)
print("-"* 100)

# select data from user input
email = input("Enter an email: ")
cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
rows = cursor.fetchall()
print("Data selected from the table")

for row in rows:
    print(row)

print("-"* 100)

# truncate data from the table
cursor.execute("TRUNCATE TABLE users")
print("Data truncated from the table")

print("-"* 100)

conn.close()
print("Connection closed")