from flask import Blueprint, render_template, redirect
from ..forms import SimpleForm
from app.models import SimplePerson, db


bp = Blueprint("simple", __name__, "")


@bp.route('/simple-form',  methods=["GET"])
def form():
    form = SimpleForm()
    return render_template("simple_form.html", form=form)


@bp.route('/simple-form', methods=["POST"])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        data = form.data
        new_user = SimplePerson(name=data['name'],
                                age=data['age'],
                                bio=data['bio'],)
        db.session.add(new_user)
        db.session.commit()

        return redirect("/", 302)
    else:
        return "Bad Data"
