import sqlite3

data = sqlite3.connect("database.db")

cursor = data.cursor()

cursor.execute('''CREATE TABLE slap
                                (id real, link text)''')
database = open("BruteData/Slap_Gifs.txt", "r")

n = 0
for i in database:
    cursor.execute(f"INSERT INTO slap VALUES ({n}, '{i}')")
    n += 1

data.commit()
