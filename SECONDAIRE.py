from sqlite3 import OperationalError
import sqlite3


class DatabaseClass:
    def __init__(self):
        self.nameDatabase = "/city_database.sq3"
        try:
            self.dataBaseConnection = sqlite3.connect(self.nameDatabase)
            self.cur = self.dataBaseConnection.cursor()
        except OperationalError:
            print("It wasn't possible to connect to the requested file.")

    def request_database(self,request):
        self.cur.execute(request)

    def close_database(self):
        self.cur.close()
        self.dataBaseConnection.close()

    def list_database(self):
        self.request_database("SELECT * FROM Cities")
        # store in memory
        list_cities_database = None
        list_cities_database = self.cur.fetchall()
        return list_cities_database

    def update_database(self, text_to_be_replaced, id_object, column_object):
        print("Updating database")
        if column_object == 0:
            self.cur.execute("UPDATE Cities SET Name=? WHERE Id=?", (text_to_be_replaced, id_object))
        elif column_object == 1:
            self.cur.execute("UPDATE Cities SET Identification=? WHERE Id=?", (text_to_be_replaced, id_object))
        elif column_object == 2:
            self.cur.execute("UPDATE Cities SET Coordinates=? WHERE Id=?", (text_to_be_replaced, id_object))
        self.dataBaseConnection.commit()

    def add_to_database(self,text_to_add, identification_to_add, coordinates_to_add):
        self.cur.execute("INSERT INTO Cities VALUES(NULL,?,?,?)", (text_to_add,identification_to_add,coordinates_to_add))
        self.dataBaseConnection.commit()
