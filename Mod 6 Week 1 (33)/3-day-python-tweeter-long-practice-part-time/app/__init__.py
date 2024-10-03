from flask import Flask, render_template
from random import choice
from .tweets import tweets

from app.config import Config #this is like a file path, could also do .config bc they're both on the same file level

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    tweet = choice(tweets)
    print(tweet)
    return render_template("index.html", tweet=tweet)


@app.route('/feed')
def feed():
    return render_template("feed.html", tweets=tweets)
