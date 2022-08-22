DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = 'gbrhex01'
DB_HOST = 'localhost'
DB_PORT = 5432
from datetime import date
import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, port=DB_PORT, host=DB_HOST)

# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a query
try:
    cur.execute("SELECT * FROM fiap.test")
except Exception as e:
    print('Excess', e)
    pass
# Retrieve query results
records = cur.fetchall()

for i in records:
    print(i[0],i[1])

#cur.execute("insert into fiap.test values('2022-07-07','23:23')")
#conn.commit()
