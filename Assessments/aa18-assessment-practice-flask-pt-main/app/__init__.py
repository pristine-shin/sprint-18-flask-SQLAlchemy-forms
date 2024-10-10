from flask import Flask, render_template
from .config import Configuration
from .models import db
from .routes import simple

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(simple.bp)
db.init_app(app)



@app.route('/')
def index():
    return render_template("main_page.html")
