from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():
    return "Welcome to Flask Application"

if __name__ == "__main__":
    application.run()
