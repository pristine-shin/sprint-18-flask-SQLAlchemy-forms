from flask import Blueprint, render_template
from ..forms import SimpleForm


bp = Blueprint("simple", __name__, url_prefix="/simple-form")

@bp.route('/')
def index():
    form = SimpleForm()
    return render_template("simple_form.html", form=form)
