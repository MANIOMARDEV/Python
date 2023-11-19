from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []

    return render_template('index.html', activities=session['activities'], gold=session['gold'])

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    earnings = 0

    if building == 'farm':
        earnings = random.randint(10, 20)
    elif building == 'cave':
        earnings = random.randint(5, 10)
    elif building == 'house':
        earnings = random.randint(2, 5)
    elif building == 'casino':
        earnings = random.randint(-50, 50)

    session['gold'] += earnings

    if earnings >= 0:
        message = f"Earned {earnings} gold from the {building}!"
        color = "green"
    else:
        message = f"Entered a casino and lost {-earnings} gold... Ouch..."
        color = "red"

    session['activities'].insert(0, {'message': message, 'color': color})

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)