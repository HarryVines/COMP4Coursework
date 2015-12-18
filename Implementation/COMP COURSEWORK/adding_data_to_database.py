import sqlite3

def insert_data(values):
    with sqlite3.connect("suppliers.db") as db:
        cursor = db.cursor()
        sql = "insert into Supplier(CompanyName,OwnerName,Address,EmailAddress,TelephoneNumber,Website) values(?,?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    information = ("ExampleName","ExampleOwnerName","ExampleAddress","Example@Example.com", "01010234323","www.Example.com")
    insert_data(information)
