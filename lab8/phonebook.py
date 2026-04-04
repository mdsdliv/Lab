import psycopg2
from config import DB_CONFIG

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def main():
    while True:
        print("\n--- PHONEBOOK (Practice 8) ---")
        print("1. Поиск контакта (ILIKE поиск)")
        print("2. Добавить/Обновить один контакт (Upsert)")
        print("3. Массовая вставка (Bulk Insert с валидацией)")
        print("4. Показать список с пагинацией (Limit/Offset)")
        print("5. Удалить контакт (по имени или телефону)")
        print("0. Выход")
        
        choice = input("\nВыберите действие: ")

        if choice == '1':
            pattern = input("Введите часть имени или номера: ")
            call_search(pattern)
        elif choice == '2':
            name = input("Имя: ")
            phone = input("Телефон: ")
            call_upsert(name, phone)
        elif choice == '3':
            # Пример списка для вставки
            names = ["Sanzhar", "Aigerim", "Bad_Contact"]
            phones = ["87071112233", "87475556677", "123"] # 123 не пройдет валидацию в базе
            call_bulk_insert(names, phones)
        elif choice == '4':
            limit = int(input("Сколько записей показать? "))
            offset = int(input("Сколько записей пропустить? "))
            call_pagination(limit, offset)
        elif choice == '5':
            target = input("Введите имя или номер для удаления: ")
            call_delete(target)
        elif choice == '0':
            print("Выход...")
            break
        else:
            print("Неверный ввод, попробуй еще раз.")

# --- Функции вызова базы ---

def call_search(p):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (p,))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

def call_upsert(name, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    print("Выполнено!")
    cur.close()
    conn.close()

def call_bulk_insert(names, phones):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("CALL bulk_insert(%s, %s)", (names, phones))
        conn.commit()
        print("Запрос на массовую вставку отправлен.")
    except Exception as e:
        print(f"Ошибка: {e}")
    cur.close()
    conn.close()

def call_pagination(limit, offset):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    for row in cur.fetchall():
        print(f"Name: {row[0]}, Phone: {row[1]}")
    cur.close()
    conn.close()

def call_delete(target):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL delete_contact(%s)", (target,))
    conn.commit()
    print("Запись удалена (если она существовала).")
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()