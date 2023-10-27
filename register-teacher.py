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

@app.route('/register-teacher.html')
def registration_form():
    return render_template('register-teacher.html')

@app.route('/register', methods=['GET','POST'])
def register():
    cursor = db.cursor()
    full_name = request.form['full_name']
    Email = request.form['Email']
    Department= request.form['Department']
    Year = request.form['Year']
    username=request.form['username']
    password=request.form['password']
    

    insert_query = "INSERT INTO faculty (full_name,Email,Department,Year,username,password,) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(insert_query, (full_name,Department,Email,password,Year))
    db.commit()

    

    cursor.close()
    return "Registration successful."

if __name__ == '__main__':
    app.run(debug=True)