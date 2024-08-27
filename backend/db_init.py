import sqlite3

connection = sqlite3.connect("todolist.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Todo (
id INTEGER PRIMARY KEY AUTOINCREMENT,
text TEXT NOT NULL
)
''')

connection.commit()
connection.close()
