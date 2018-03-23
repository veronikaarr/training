import sqlite3

conn = sqlite3.connect('test2.db')

conn.execute('''insert into sample(column2, column2, column3, column4) values(1, "Record 1 Text A", "Record 1 Text B", 3.14159);''')
conn.execute('''insert into sample(column1, column2, column3, column4) values(2, "Record 2 Text A", "Record 2 Text B", 6.28318);''')
conn.execute('''insert into sample(column1, column2, column3, column4) values(3, "Record 3 Text A", "Record 3 Text B", 9.42477);''')
conn.commit()
