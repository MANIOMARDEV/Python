from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1

    return render_template('index.html', counter=session['counter'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('index'))

@app.route('/increment', methods=['POST'])
def increment():
    if 'counter' not in session:
        session['counter'] = 0
    increment_value = int(request.form.get('increment_value', 1))
    session['counter'] += increment_value
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
