from flask import Flask
import Betfair.FootballDriver

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello"


app.run()
