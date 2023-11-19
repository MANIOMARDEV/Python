from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Retrieve form data
    name = request.form['name']
    email = request.form['email']
    radio_option = request.form['radio_option']
    checkbox_options = request.form.getlist('checkbox_options')

    # Save form data to session
    session['name'] = name
    session['email'] = email
    session['radio_option'] = radio_option
    session['checkbox_options'] = checkbox_options

    return redirect(url_for('result'))

@app.route('/result')
def result():
    # Retrieve form data from session
    name = session.get('name', '')
    email = session.get('email', '')
    radio_option = session.get('radio_option', '')
    checkbox_options = session.get('checkbox_options', [])

    return render_template('result.html', name=name, email=email, radio_option=radio_option, checkbox_options=checkbox_options)

if __name__ == '__main__':
    app.run(debug=True)
