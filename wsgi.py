from flask import Flask
application = Flask(__name__)

@application.route("/hello")
def hello():
    return "I love Khalid V2!"

if __name__ == "__main__":
    application.run()
