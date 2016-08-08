from flask import Flask, render_template, request, Markup
from prime_finder import PrimeFinder

# Declare and initialize application
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
@application.route('/<int:occurrence>/<int:digits>')
def rest_compute(occurrence, digits):
    return render_template(
        'home.html',
        occurrence=occurrence,
        digits=digits,
        result=compute(occurrence, digits)
    )


# Enable upload calls
@application.route('/upload', methods=['POST', 'GET'])
def upload():
    results = []
    if request.method == 'POST':
        for line in request.files['tuples']:
            csv_tuple = line.split(',')
            results.append({
                'occurrence': csv_tuple[0],
                'digits': csv_tuple[1],
                'value': compute(csv_tuple[0], csv_tuple[1])
            })
    return render_template(
        'home.html',
        results=results
    )


def compute(occurrence, digits):
    finder = PrimeFinder()

    try:
        occurrence = int(occurrence)
        digits = int(digits)
    except ValueError:
        return Markup(
            "<strong>Error: both values must be valid integers</strong>"
        )

    if occurrence > 0 and digits > 0:
        return Markup(
            "<em>%d</em>" % finder.prime_of_length(occurrence, digits)
        )

    return Markup(
        "<strong>Error: values must be positive integers</strong>"
    )


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

