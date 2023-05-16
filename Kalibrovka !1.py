import sqlite3


with sqlite3.connect("id_chat.db") as connect:
    cursor = connect.cursor()
    cursor.execute(f"SELECT * FROM memori WHERE id_chat = {123}")
    res = cursor.fetchone()
    print(res)
    cursor.execute(f"UPDATE memori SET word = 'table1' WHERE id_chat = {123}")
    res1 = cursor.fetchone()
    print(res1)

    rows = cursor.fetchall()
    for row in rows:
        print(row)



    cursor.close()




