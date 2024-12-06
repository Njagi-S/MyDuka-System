import psycopg2


conn = psycopg2.connect(database="myduka", user="postgres", password="test@test", host="localhost",port="5432")
cur = conn.cursor()
print("Database connected successfully")