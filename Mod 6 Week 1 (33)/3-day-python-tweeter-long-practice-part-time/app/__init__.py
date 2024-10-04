from flask import Flask, render_template
from .tweets import tweets
from random import choice
from .routes.tweets_routes import tweets_router
from app.form.form import TweetForm


from app.config import Config #this is like a file path, could also do .config bc they're both on the same file level

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(tweets_router) #could also prefix the url here, needs to just be in one place

@app.route('/')
def index():
    tweet = choice(tweets)
    print(tweet)
    return render_template("index.html", tweet=tweet)

@app.route('/new')
def new():
    form = TweetForm()
    return render_template("new_tweet.html", form=form)
