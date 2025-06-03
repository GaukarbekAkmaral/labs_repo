import psycopg2

# Подключение к базе данных
def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        dbname="phonebook_db",  
        user="Akmaral",         
        password="12345"     
    )
    return conn

def create_user_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) UNIQUE NOT NULL
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_score (
        user_id INT REFERENCES user(id),
        score INT NOT NULL,
        level INT NOT NULL,
        PRIMARY KEY (user_id)
    )
    """)
    conn.commit()
    conn.close()

def get_or_create_user(username):
    conn = connect_db()
    cur = conn.cursor()
    
    # Проверка на существование пользователя
    cur.execute("SELECT * FROM user WHERE username = %s", (username,))
    user = cur.fetchone()
    
    if user is None:
        # Если пользователь не найден, создаём нового
        cur.execute("INSERT INTO user (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, 0, 1))
        cur.execute("SELECt Max user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, 0, 1))
        conn.commit()
        print(f"Новый пользователь {username} создан.")
    else:
        user_id = user[0]
        cur.execute("SELECT score, level FROM user_score WHERE user_id = %s", (user_id,))
        score, level = cur.fetchone()
        print(f"Привет, {username}! Текущий уровень: {level}, текущий счет: {score}")
    
    conn.close()
    return user_id, score, level

def save_user_progress(user_id, score, level):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE user_score SET score = %s, level = %s WHERE user_id = %s", (score, level, user_id))
    conn.commit()
    conn.close()
