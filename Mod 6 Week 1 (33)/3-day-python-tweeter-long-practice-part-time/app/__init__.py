from flask import Flask, render_template, redirect
from .tweets import tweets
import random
from random import choice
from .routes.tweets_routes import tweets_router
from app.form.form import TweetForm
from datetime import date


from app.config import Config #this is like a file path, could also do .config bc they're both on the same file level

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(tweets_router) #could also prefix the url here, needs to just be in one place

@app.route('/')
def index():
    tweet = choice(tweets)
    print(tweet)
    return render_template("index.html", tweet=tweet)

@app.route('/new', methods=['GET', 'POST'])
def new():
    form = TweetForm()
    today = date.today()
    formatted_date = today.strftime("%m/%d/%y")
    if form.validate_on_submit():
        new_tweet = {
            'id': len(tweets),
            'author': form.data['author'],
            'tweet': form.data['tweet'],
            'date': formatted_date,
            'likes': random.randint(100000, 999999)
        }

        tweets.append(new_tweet)

        return redirect('/tweets/feed', 302)

    if form.errors:
        return form.errors

    return render_template("new_tweet.html", form=form)
