import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

if __name__ == '__main__':
    sql = input("Enter sql --> ")
    connection = sqlite3.connect("test2.db")
    connection.row_factory = dict_factory
    cursor = connection.cursor()

    try:
        cursor.execute(sql)
    except sqlite3.OperationalError:
        print("Incorrectly entered data")
 
    results = cursor.fetchall()
    print(results)
    connection.close()

