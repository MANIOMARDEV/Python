from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)


@app.route('/users/new')
def new_user():
    return render_template('create.html')

@app.route('/create' , methods = ['post'])
def create():
    data = request.form
    User.create(data)

    return redirect('/users')

@app.route('/users')
def users():
    users = User.get_all()

    return render_template('read.html', users = users)

if __name__ == "__main__":
    app.run(debug = True)