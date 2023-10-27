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

@app.route('/Register-student.html')
def registration_form():
    return render_template('Register-student.html')

@app.route('/register', methods=['GET','POST'])
def register():
    cursor = db.cursor()
    full_name = request.form['full_name']
    prn = request.form['prn']
    S_Department= request.form['Department']
    S_email = request.form['Email']
    S_password=request.form['password']
    Year = request.form['Year']
    

    insert_query = "INSERT INTO student (full_name,prn,S_department,S_email,S_password,Year) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(insert_query, (full_name,prn,S_Department,S_email,S_password,Year))
    db.commit()

    

    cursor.close()
    return "Registration successful."

if __name__ == '__main__':
    app.run(debug=True)