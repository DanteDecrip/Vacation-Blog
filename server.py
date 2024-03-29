from flask import Flask, redirect, render_template, request, session

from orm import Users

app = Flask(__name__) 
app.secret_key = 'lame_key'

@app.route('/')
def home_page():
    return render_template('name_template.html')

@app.route('/create_page')
def create_user_page():
    return render_template('create_page.html')

@app.route('/new_user')
def new_user():
    Users().create(request.form['uname'], request.form['password'])


@app.route('/login_page')
def login_page():
    return render_template('login_page.html')

@app.route('/credentials', methods=['post'])
def logon():
    attempted_user = Users().get(request.form['uname'])

    if attempted_user is None or attempted_user['password'] != request.form['password']:
        return redirect('/login_page')
    else:
        session['username'] = attempted_user['username']
        return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)