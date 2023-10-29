import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123',
    database='projectmanagementsystem'
)
cursor = db.cursor()
try:
    insert_query = "INSERT INTO student (full_name,prn,S_Department,S_email,S_password,Year,Roll_no,batch) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(insert_query, ('wwww1', '2122231', 'csewe1', 'hferrgh@gmail.com1', '134231', '2', 'syb2522', 'b241'))
    db.commit()
except mysql.connector.errors.IntegrityError as e:
    if e.errno == 1062:
        print("Duplicate entry detected. You may want to update or delete the existing record.")
    else:
        print(f"An IntegrityError occurred: {e}")
    # Handle the error as needed
except mysql.connector.Error as e:
    print(f"A MySQL error occurred: {e}")
    
