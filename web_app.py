from flask import Flask, render_template, request, Markup
from prime_finder import PrimeFinder

# Declare and initialize application
application = Flask(__name__)


# Default route, root of website directory
@application.route('/', methods=['POST', 'GET'])
def home():
    """
    Handle the request for the home page (root directory of web app)

    :return: home.html page by default, rest_compute()
    method when a 'POST' request is submitted
    """
    if request.method == 'POST':
        return rest_search(
            request.form['occurrence'],
            request.form['digits']
        )
    return render_template('home.html')


# Enable REST calls directly to computation
@application.route('/<int:occurrence>/<int:digits>')
def rest_search(occurrence, digits):
    """
    Handle prime-tuple search by URL REST request

    :param occurrence: Xth occurrence of any prime
    :param digits: Y-digit size of any prime
    :return: home.html page with initial variables, plus
    result value of the search
    """
    return render_template(
        'home.html',
        occurrence=occurrence,
        digits=digits,
        result=search(occurrence, digits)
    )


# Enable upload calls, searches done by CSV file
@application.route('/upload', methods=['POST', 'GET'])
def upload_search():
    """
    Accept an uploaded file (.csv) and perform searches
     using tuples within the file. Since the file is
     expected to be a .csv, lines will be tuples of two
     numbers separated by a comma. However, checks must
     still be made to ensure integrity of input values
     and file format.

     Initialize empty list to hold results. For each line
     in the uploaded file, split by comma-delimiter and
     store in smaller list. If the split list is larger
     than 1 in size, then use first two list entries as
     parameters for search. Otherwise, throw error notifying
     user of the problem for the expected tuple. Store
     each search result as a three-value tuple in a
     dictionary and append it to results list.

    :return: home.html with a results parameter assigned
    to the results list
    """
    results = []
    if request.method == 'POST':
        for line in request.files['tuples']:
            if line.strip() != "":
                csv_tuple = line.split(',')
                if len(csv_tuple) > 1:
                    results.append({
                        'occurrence': csv_tuple[0],
                        'digits': csv_tuple[1],
                        'value': search(csv_tuple[0], csv_tuple[1])
                    })
                else:
                    results.append({
                        'occurrence': csv_tuple[0].strip(),
                        'digits': '??',
                        'value': Markup('<strong>Error: Missing a value</strong>')
                    })
    return render_template(
        'home.html',
        results=results
    )


def search(occurrence, digits):
    """
    Helper method, responsible for searching for primes of
    specified parameters. Handles most of the error-handling
    and result-relay from the PrimeFinder object.

     Uses the PrimeFinder object to search for Xth occurrence
     of Y-digit prime within Euler's Number. Uses default
     instance-assigned precision, which is currently 200-digit
     precision.

     Try to convert parameters to int before performing search.
     This conversion is mostly for form values that get passed
     as Unicode strings and require conversion. Ensure that both
     parameters are positive before searching and notify user of
     no results if search turns up empty.

    :param occurrence: Xth occurrence of any prime
    :param digits: Y-digit size of any prime
    :return: search result if found, informative message otherwise
    """
    finder = PrimeFinder()

    try:
        occurrence = int(occurrence)
        digits = int(digits)
    except ValueError:
        return Markup(
            "<strong>Error: both values must be valid integers</strong>"
        )

    if occurrence > 0 and digits > 0:
        if digits <= PrimeFinder.DIGIT_LIMIT:
            result = finder.prime_of_length(occurrence, digits)
            if result < 0:
                return Markup(
                    "<strong>Sorry, couldn't find that with current precision</strong>"
                )
            return Markup(
                "<em>%d</em>" % result
            )
        else:
            return Markup(
                "<strong>Woah, there! Too many digits.</strong>"
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

