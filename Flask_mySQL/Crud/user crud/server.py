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

@app.route('/users/<int:user_id>')
def get_by_id(user_id):
    user = User.get_by_id({'id': user_id})
    if user:
        return render_template('view.html' , user = user)
    return redirect('/users')

@app.route('/users/<int:user_id>/edit')
def update_user(user_id):
    user = User.get_by_id({'id': user_id})
    if user: 
        return render_template("edit.html" , user = user)
    return redirect("/users")

@app.route('/update' , methods = ['post'])
def update():
    data = request.form
    res = User.update_user(data)
    return redirect('/users')

@app.route('/users/<int:user_id>/delete')
def delete(user_id):
    User.delete_user({'id': user_id})
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug = True)