from flask import Flask, render_template, request, session

import random

app = Flask(__name__)
app.secret_key = "greatnumgame"


@app.route("/")
def num_game():
    guess_number = random.randrange(0, 101)
    if "guess" not in session:
        session["guess"] = guess_number
    return render_template("number_game.html")


@app.route("/check", methods=["POST"])
def check_input_value():
    try:
        input_value = int(request.form["input_guess"])
    except ValueError:
        box_color = "yellow"  # You can choose a color for invalid input
        box_text = "Please enter a valid number!"
        return render_template("number_game.html", box_color=box_color, box_text=box_text)

    random_guess = session["guess"]
    box_color = ""
    box_text = ""
    reset_button = ""

    if input_value == random_guess:
        box_color = "green"
        box_text = "You've Guessed the number!"
        reset_button = '<a href="/"><button type="submit" class="btn btn-primary subbut" value="Submit">Try Again</button></a>'
        session.clear()
    elif input_value > random_guess:
        box_color = "red"
        box_text = "Your guess is too high! Try again!"
    elif input_value < random_guess:
        box_color = "blue"
        box_text = "Your guess is too low! Try again!"

    return render_template("number_game.html", box_color=box_color, box_text=box_text, reset_button=reset_button)


if __name__ == "__main__":
    app.run(debug=True)
