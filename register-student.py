from flask import Flask, request, render_template,session,redirect,url_for
import mysql.connector

app=Flask(__name__)


db = {
    'host':'localhost',
    'user':'root',
    'password':'Anuja@2002',
    'database':'projectmanagementsystem'
}

@app.route('/')
def registration_form():
    return render_template('register_student.html')

# @app.route('/Register-student.html',methods=['GET','POST'])
# def registration_form():
#     print(request.args)
#     return render_template('register_student.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        
        full_name = request.form['fullname']
        S_email = request.form['email']
        S_Department= request.form['department']
        Year = request.form['year']
        Roll_no=request.form['RollNo']
        batch=request.form['Batch']
        prn = request.form['username']
        S_password=request.form['password']

        try:
    
            con=mysql.connector.connect(**db)
            cursor = con.cursor()
        
        

            insert_query = "INSERT INTO student (full_name,prn,S_Department,S_email,S_password,Year,Roll_no,batch) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            data=(full_name,prn,S_Department,S_email,S_password,Year,Roll_no,batch)
            cursor.execute(insert_query,data )
            con.commit()
            cursor.close()
            con.close()

            return "Registration successful."
        except Exception as e:
            return str(e)



if __name__ == '__main__':
    app.run(debug=True)
