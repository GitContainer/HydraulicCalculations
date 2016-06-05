import sqlite3

i = 1
if i == 0:
    cities = (
                ("Dunkerque","59183001","Alt : 11 m, lat : 51°03-18-N, lon : 02°20-18-E"),
                ("Lille","59180000","Alt : 50m"),
                ("Boulogne","62150000","Alt : 80")
              )

    dataBase = sqlite3.connect("/city_database.sq3")
    cur = dataBase.cursor()
    tb_exists = "SELECT * FROM Cities"
    print("Beginning error")
    cur.execute("DROP TABLE IF EXISTS Cities")
    cur.execute("CREATE TABLE Cities(reference INTEGER PRIMARY KEY,Name TEXT,Identification TEXT, Coordinates TEXT)")
    cur.executemany("INSERT INTO Cities VALUES(NULL,?,?,?)", cities)
    cur.execute(tb_exists)
    data = cur.fetchall()
    print(data)
    dataBase.commit()
else:
    dataBase = sqlite3.connect("/city_database.sq3")
    cur = dataBase.cursor()
    cur.execute("SELECT * FROM Cities")
    rows = cur.fetchall()
    print(rows)
