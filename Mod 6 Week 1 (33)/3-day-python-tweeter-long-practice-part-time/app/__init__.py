from flask import Flask

from app.config import Config #this is like a file path, could also do .config bc they're both on the same file level

app = Flask(__name__)
app.config.from_object(Config)
