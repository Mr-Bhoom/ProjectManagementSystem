from flask import Flask, request, render_template,session
import mysql.connector

app=Flask(__name__)


db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123',
    database='projectmanagementsystem'
)
@app.route('/')

@app.route('/Register-student.html',methods=['GET','POST'])
def registration_form():
    print(request.args)
    return render_template('Register-student.html')

@app.route('/register', methods=['GET','POST'])
def register():
    cursor = db.cursor()
    full_name = request.form.get['fullname']
    S_email = request.form.get['email']
    S_Department= request.form.get['department']
    Year = request.form.get['year']
    Roll_no=request.form.get['RollNo']
    batch=request.form.get['Batch']
    prn = request.form.get['username']
    S_password=request.form.get['password']
    
  
    
    

    insert_query = "INSERT INTO student (full_name,prn,S_Department,S_email,S_password,Year,Roll_no,batch) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(insert_query, (full_name,prn,S_Department,S_email,S_password,Year,Roll_no,batch))
    db.commit()

    

    cursor.close()
    return "Registration successful."

if __name__ == '__main__':
    app.run(debug=True)