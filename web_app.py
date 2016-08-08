from flask import Flask, render_template, request
from prime_finder import PrimeFinder

# EB looks for an 'application' callable by default.
application = Flask(__name__)


# Default route, root of website directory
@application.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return rest_compute(
            request.form['occurrence'],
            request.form['digits']
        )
    return render_template('home.html')


# Enable REST calls directly to computation
@application.route('/<occurrence>/<digits>')
def rest_compute(occurrence, digits):
    return render_template(
        'home.html',
        occurrence=occurrence,
        tuple=digits,
        result=compute(occurrence, digits)
    )


# Enable upload calls
@application.route('/upload', methods=['POST', 'GET'])
def upload():
     # TODO implement file upload
    return "Don't forget to implement me!"


def compute(occurrence, digits):
    finder = PrimeFinder()

    try:
        occurrence = int(occurrence)
        digits = int(digits)
    except ValueError:
        return "Error: input values must be integers"

    return finder.prime_of_length(occurrence, digits)


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

