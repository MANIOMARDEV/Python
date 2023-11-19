from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'secret_key'

def generate_new_number():
    return random.randint(1, 100)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = generate_new_number()
        session['attempts'] = 0
        session['message'] = ''

    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['attempts'] += 1

        if guess == session['number']:
            message = f'Congratulations! You guessed the correct number in {session["attempts"]} attempts.'
            session.pop('number')
            session.pop('attempts')
            session['message'] = message
            return redirect(url_for('index'))

        elif guess < session['number']:
            session['message'] = 'Too low! Try again.'

        else:
            session['message'] = 'Too high! Try again.'

    return render_template('index.html', message=session['message'])

@app.route('/leaderboard')
def leaderboard():
    # You can implement a leaderboard here, storing winners' names and attempts in a database
    return render_template('leaderboard.html')

if __name__ == '__main__':
    app.run(debug=True)
