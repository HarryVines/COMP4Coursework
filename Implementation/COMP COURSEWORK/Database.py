import sqlite3

class Database:
    def __init__(self,db_name):
        self._db_name = db_name
        self.create_tables()

    def execute_sql(self,sql):
        with sqlite3.connect(self._db_name) as db:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
    def GetAllSuppliers(self):
        with sqlite3.connect(self._db_name) as db:
            cursor = db.cursor()
            cursor.execute("select * from Supplier")
            suppliers = cursor.fetchall()
            return suppliers
        
    def create_tables(self):
        sql = """CREATE TABLE IF NOT EXISTS Supplier 
                 (SupplierID int primary key,
                 CompanyName text,
                 OwnerName text,
                 Address text,
                 EmailAddress text,
                 TelephoneNumber text,
                 Website text)"""
        self.execute_sql(sql)

        sql = """CREATE TABLE IF NOT EXISTS Parts
                 (PartName text,
                 PartPrice text)"""
        self.execute_sql(sql)

        sql = """CREATE TABLE IF NOT EXISTS Comments
                (Comment text,
                Rating integer)"""
        self.execute_sql(sql)

    def insert_data(self,values):
        with sqlite3.connect("suppliers.db") as db:
            cursor = db.cursor()
            sql = "insert into Supplier(CompanyName,OwnerName,Address,EmailAddress,TelephoneNumber,Website) values(?,?,?,?,?,?)"
            cursor.execute(sql,values)
            db.commit()

    def add_supplier(self,name,oname,address,email,telephone,website):
        sql = """INSERT INTO Supplier(CompanyName, OwnerName, Address, EmailAddress, TelephoneNumber, Website) values
                 ('{0}',
                 '{1}',
                 '{2}',
                 '{3}',
                 '{4}',
                 '{5}')""".format(name,oname,address,email,telephone,website)
        self.execute_sql(sql)

    def add_comment(self,comment,rating):
        sql = """INSERT INTO Comments(Comment, Rating) values
                 ('{0}',
                 '{1}')""".format(comment,rating)
        self.execute_sql(sql)

    def view_suppliers(self):
        sql = """SELECT * FROM Supplier"""
        self.execute_sql(sql)
        
g_database = Database("Suppliers.db")
