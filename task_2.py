# Задача 2: Создать таблицу с тремя колонками. Заполнить ее тремя записями.

import sqlite3

connection = sqlite3.connect('siser.db')

cursor = connection.cursor()

# cursor.execute('CREATE TABLE doso (age INTEGER, name TEXT, surname TEXT)')

cursor.execute("INSERT INTO doso (age, name, surname ) VALUES (59, 'Siarhei', 'SIDORCHYK')")
cursor.execute("INSERT INTO doso (age, name, surname) VALUES (25, 'Ivan', 'Ivanov')")
cursor.execute("INSERT INTO doso (age, name, surname) VALUES (30, 'Petr', 'Petrov')")

connection.commit()

connection.close()