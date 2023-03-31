import sqlite3
base = sqlite3.connect('DZ.db')
cursor = base.cursor()

base.execute('''CREATE TABLE IF NOT EXISTS table1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
base.commit()

cursor.execute('''INSERT INTO table1(col_1, col_2) VALUES ('1 ',"2")''')
base.commit()

cursor.execute('''SELECT * FROM table1''')
cursor.execute('''DELETE FROM table1 WHERE id%2 = 0''')
base.commit()

cursor.execute('''SELECT * FROM table1''')
cursor.execute('''UPDATE table1 SET col_1=5, col_2=8''')
base.commit()

cursor.execute('''SELECT * FROM table1''')
k = cursor.fetchall()
for i in k:
    print (i)
base.close()

