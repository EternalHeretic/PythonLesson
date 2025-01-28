# Задача "Средний баланс пользователя":
# Для решения этой задачи вам понадобится решение предыдущей.
# Для решения необходимо дополнить существующий код:
# Удалите из базы данных not_telegram.db запись с id = 6.
# Подсчитать общее количество записей.
# Посчитать сумму всех балансов.
# Вывести в консоль средний баланс всех пользователей.
#
# Пример результата выполнения программы:
# Выполняемый код:
# # Код из предыдущего задания
# # Удаление пользователя с id=6
# # Подсчёт кол-ва всех пользователей
# # Подсчёт суммы всех балансов
# print(all_balances / total_users)
# connection.close()
#
# Вывод на консоль:
# 700.0

import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

cursor.execute('''
UPDATE Users
SET balance = 500
WHERE id IN (SELECT id FROM Users WHERE id % 2 = 1)
''')

cursor.execute('''
DELETE FROM Users
WHERE id IN (SELECT id FROM Users WHERE (id - 1) % 3 = 0)
''')

cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

if total_users > 0:
    average_balance = all_balances / total_users
    print(average_balance)
else:
    print("Нет пользователей в таблице.")

conn.commit()
conn.close()