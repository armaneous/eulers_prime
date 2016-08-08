from flask import Flask

# EB looks for an 'application' callable by default.
application = Flask(__name__)


# Default route, root of website directory
@application.route('/')
def home():
    return "Hello World!"


# Enable REST calls directly to computation
@application.route('/<occurrence>/<tuple>')
def rest_compute(occurrence, tuple):
    # TODO Bonus: evaluate by REST call
    return "Values %s, %s" % (occurrence, tuple)


# Enable upload calls
@application.route('/upload', methods=['POST', 'GET'])
def upload():
     # TODO implement file upload
    return "Don't forget to implement me!"


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

