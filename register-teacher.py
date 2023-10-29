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
    f_username=request.form['username']
    full_name = request.form['fullname']
    password=request.form['password']
    Email = request.form['email']
    Department= request.form['Department']
    
    
    

    insert_query = "INSERT INTO faculty (f_username,full_name,password,Email,Department) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(insert_query, (f_username,full_name,password,Email,Department))
    cursor.commit()

    

    cursor.close()
    return "Registration successful."

if __name__ == '__main__':
    app.run(debug=True)