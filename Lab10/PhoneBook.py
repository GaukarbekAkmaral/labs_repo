import psycopg2
import csv

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook_db",      
    user="Akmaral",             
    password="12345"            
)
cur = conn.cursor()

# Создание таблицы, если не существует
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL
)
""")
conn.commit()

# Вставка из CSV
def insert_from_csv():
    file_path = input("Введите путь к CSV файлу: ")
    try:
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader)  
            for row in reader:
                cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (row[0], row[1]))
        conn.commit()
        print("✅ Данные успешно загружены из CSV.")
    except Exception as e:
        print("⚠️ Ошибка при загрузке из CSV:", e)

# Ввод данных вручную
def insert_from_input():
    username = input("Введите имя пользователя: ")
    phone = input("Введите номер телефона: ")
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
    conn.commit()
    print("✅ Данные успешно добавлены.")

# Обновление данных
def update_data():
    choice = input("Что вы хотите обновить? (1) имя, (2) телефон: ")
    if choice == '1':
        old_name = input("Введите текущее имя: ")
        new_name = input("Введите новое имя: ")
        cur.execute("UPDATE phonebook SET username = %s WHERE username = %s", (new_name, old_name))
    elif choice == '2':
        name = input("Введите имя пользователя для изменения телефона: ")
        new_phone = input("Введите новый телефон: ")
        cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (new_phone, name))
    conn.commit()
    print("✅ Обновление выполнено.")

# Поиск
def search_phonebook():
    print("Поиск: (1) Все, (2) По имени, (3) По номеру")
    choice = input("Выберите опцию: ")
    if choice == '1':
        cur.execute("SELECT * FROM phonebook")
    elif choice == '2':
        name = input("Введите имя: ")
        cur.execute("SELECT * FROM phonebook WHERE username ILIKE %s", ('%' + name + '%',))
    elif choice == '3':
        phone = input("Введите телефон: ")
        cur.execute("SELECT * FROM phonebook WHERE phone ILIKE %s", ('%' + phone + '%',))
    
    rows = cur.fetchall()
    print("\n📞 Найденные записи:")
    for row in rows:
        print(row)

# Удаление
def delete_data():
    choice = input("Удалить по: (1) имени, (2) телефону: ")
    if choice == '1':
        name = input("Введите имя: ")
        cur.execute("DELETE FROM phonebook WHERE username = %s", (name,))
    elif choice == '2':
        phone = input("Введите телефон: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()
    print("✅ Удаление завершено.")

# Главное меню
def main():
    while True:
        print("\n📱 Меню PhoneBook:")
        print("1. Добавить из CSV")
        print("2. Добавить вручную")
        print("3. Обновить запись")
        print("4. Найти запись")
        print("5. Удалить запись")
        print("6. Выход")

        option = input("Выберите опцию (1-6): ")

        if option == '1':
            insert_from_csv()
        elif option == '2':
            insert_from_input()
        elif option == '3':
            update_data()
        elif option == '4':
            search_phonebook()
        elif option == '5':
            delete_data()
        elif option == '6':
            break
        else:
            print("⚠️ Неверная опция. Попробуйте снова.")

    # Закрытие подключения
    cur.close()
    conn.close()
    print("👋 Завершение работы. До свидания!")

# Запуск
if __name__ == "__main__":
    main()
