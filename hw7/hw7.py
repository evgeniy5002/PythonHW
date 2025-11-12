import datetime

import mysql.connector

# Опис завдання:
# Д.З. Реалізувати виконання запиту, який визначає різницю
# між поточною датою та введеною користувачем, з включенням
# даних, що вводяться з консолі програми. Перед передачею
# даних до запиту здійснити попередню валідацію на правильність
# дати, а також передбачити те, що додаткову валідацію буде проведено СУБД
# Введіть дату: 2025-10-01 Дата у минулому за 28 днів від поточної дати
# Введіть дату: 2025-11-01 Дата у майбутньому через 3 дні від поточної дати
# Введіть дату: 2025-10-29 Дата є поточною

db_ini = {
    'host': 'localhost',
    'port': 3306,
    'user': 'user_knp_221',
    'password': 'pass_221',
    'database': 'server_221',
    'charset': 'utf8mb4',
    'use_unicode': True,
    'collation': 'utf8mb4_unicode_ci'
}

db_connection = None


def connect_db():
    global db_connection

    try:
        db_connection = mysql.connector.connect(**db_ini)
    except mysql.connector.Error as err:
        print(err)
    else:
        print("Connected")


def close_connection():
    db_connection.close()


def print_table(cursor):
    print(("║ " + cursor.column_names[0]).ljust(39, ' ') + ("║ " + cursor.column_names[0]).ljust(39, ' ') + "║")
    print("╠" + "═" * 38 + "╬" + "═" * 38 + "╣")

    for row in cursor:
        print("║", " ║ ".join(row), "║")


def show_prep(date: str):
    sql = "SELECT DATEDIFF(CURRENT_TIMESTAMP, STR_TO_DATE(%s, '%Y-%m-%d')) AS `date difference`"

    global db_connection

    if db_connection is None:
        return

    try:
        with db_connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, (date,))

            for row in cursor:
                diff = row["date difference"]

                if diff is None:
                    print("Invalid format")
                elif diff == 0:
                    print("Дата є поточною")
                elif diff > 0:
                    print(f"Дата у минулому за {diff} днів від поточної дати")
                elif diff < 0:
                    print(f"Дата у майбутньому через {-diff} дні від поточної дати")

    except mysql.connector.Error as err:
        print("ERR:", err)
        print("SQL:", sql)


def input_date() -> str:
    months_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    while True:
        date = input("Input date [yyyy-mm-dd]: ")

        if len(date) != 10 or not date.isdigit() and date[4] != "-" and date[7] != "-":
            print("Invalid format")
            continue

        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:10])

        if year <= 0:
            print("Invalid year")
            continue

        if month not in months_days.keys():
            print("Invalid month")
            continue

        if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            days = 29
        else:
            days = months_days[month]

        if day < 1 or day > days:
            print("Invalid day")
            continue

        return date


def main():
    connect_db()

    show_prep(input_date())
    show_prep(input_date())
    show_prep(input_date())
    show_prep(input_date())

    close_connection()


if __name__ == '__main__':
    main()
