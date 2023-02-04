from flask import Flask, request
import random

app = Flask(__name__)
secret_number = random.randint(1, 10)

@app.route("/check_guess", methods=["POST"])
def check_guess():
    guess = int(request.form["guess"])
    if guess == secret_number:
        return "You guessed the number! The secret number was {}.".format(secret_number)
    elif guess < secret_number:
        return "Your guess is too low. Try again."
    else:
        return "Your guess is too high. Try again."

if __name__ == "index.html":
    app.run()
