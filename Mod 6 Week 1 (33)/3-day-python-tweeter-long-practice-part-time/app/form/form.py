from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class TweetForm(FlaskForm):
    author = StringField("Author")
    tweet = StringField("Tweet")
    submit = SubmitField("Create Tweet")
