from flask import Flask, render_template
from flask_migrate import Migrate
from .config import Configuration
from .models import db, SimplePerson
from .routes import simple

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(simple.bp)
db.init_app(app)
Migrate(app, db)


@app.route('/')
def index():
    return render_template("main_page.html")


@app.route('/simple-form-data')
def data():
    people = SimplePerson.query.all()
    return render_template('simple_form_data.html', people=people)
