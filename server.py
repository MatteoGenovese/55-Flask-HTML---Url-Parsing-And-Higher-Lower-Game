from flask import Flask
import random

numberSelected = random.randint(1, 9)
app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<p>add to the url '/{number}' to guess</p>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:numberTyped>")
def guessNumber(numberTyped):
    if numberTyped == numberSelected:
        return "<h1 style='color: green'>You found the correct number</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    if numberTyped < numberSelected:
        return "<h1 style='color: red'>it is lower</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    if numberTyped > numberSelected:
        return "<h1 style='color: purple'>it is higher</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
