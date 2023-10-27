from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


app.secret_key = 'your_secret_key'


users = {
    'user1': 'password1',
    'user2': 'password2',
}

def check_credentials(username, password):
    if username in users and users[username] == password:
        return True
    return False

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if check_credentials(username, password):
            flash('Login successful', 'success')
            return redirect(url_for('welcome'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')

    return render_template('login-student.html')

@app.route('/welcome')
def welcome():
    return 'Welcome to the protected area!'

if __name__ == '__main__':
    app.run(debug=True)
