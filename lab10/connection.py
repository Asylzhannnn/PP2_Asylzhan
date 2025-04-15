import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",  # Пробуем подключиться к стандартной БД
        user="postgres",
        password="Asylzhan2007",
        port="5432"
    )
    print("✅ Python успешно подключен к PostgreSQL!")
    conn.close()
except Exception as e:
    print(f"❌ Ошибка подключения: {e}")
