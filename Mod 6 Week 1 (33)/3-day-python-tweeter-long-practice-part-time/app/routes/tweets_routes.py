from flask import Blueprint, render_template
from ..tweets import tweets


tweets_router = Blueprint('tweets', __name__, url_prefix="/tweets")

@tweets_router.route('/feed')
def feed():
    return render_template("feed.html", tweets=tweets)
