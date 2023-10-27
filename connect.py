import mysql.connector

try:
    db=mysql.connector.connect(host='localhost',user='root',password='123',database='projectmanagementsystem')
    cursor=db.cursor()

    db.commit()
    db.close()
    print("connection occured")
except:
    print("Exception occured")
