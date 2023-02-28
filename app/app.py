"""this module contains the main app to start the api server"""

from flask import Flask

from challenge_1 import ord_status
from challenge_2 import ord_season
from challenge_3 import weather_change

app = Flask(__name__)


@app.route("/")
def index():
    """Default index main"""
    return "<h1>Technical Test Python</h1>"


@app.route("/get_ord_status")
def get_ord_status():
    """Return status order"""
    return ord_status()


@app.route("/get_ord_season")
def get_ord_season():
    """Return season order"""
    return ord_season()


@app.route("/get_weather_change")
def get_weater_change():
    """Return weather change"""
    return weather_change()


if __name__ == "__main__":
    app.run(debug=True)
