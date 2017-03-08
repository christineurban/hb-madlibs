from random import choice, sample

from flask import Flask, render_template, request




# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():
    """Play Game?"""

    answer = request.args.get("game")

    if not answer:
        return render_template("goodbye.html")
    else:
        return render_template("game.html")



MADLIB = [ "madlib.html", "madlib2.html"]


@app.route('/madlib')
def show_madlib():
    """Madlib result."""

    person_py = request.args.get("person")
    color_py = request.args.getlist("color")
    noun_py = request.args.get("noun")
    adjective_py = request.args.get("adjective")
    plural_py = request.args.get("plural")

    color_string = ""

    for color in color_py:
      color_string += color + " "

    madlib_py = choice(MADLIB)

    return render_template(madlib_py,
                           person=person_py,
                           color=color_string,
                           noun=noun_py,
                           adjective=adjective_py,
                           plural=plural_py)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
