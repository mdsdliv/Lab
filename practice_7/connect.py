import psycopg2

def connect():
    """ Устанавливает соединение с сервером PostgreSQL """
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",      # или IP сервера
            database="your_db",    # имя твоей базы
            user="postgres",       # твой логин
            password="123"         # твой пароль
        )
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка подключения: {error}")
        return None
