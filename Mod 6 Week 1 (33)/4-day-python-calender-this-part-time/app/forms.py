from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
from wtforms.validators import DataRequired

class AppointmentForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    start_datetime = DateField("start_date", validators=[DataRequired()])
    start_datetime = TimeField("start_time", validators=[DataRequired()])
    end_datetime = DateField("end_date", validators=[DataRequired()])
    end_datetime = TimeField("end_time", validators=[DataRequired()])
    description = TextAreaField("description", validators=[DataRequired()])
    private = BooleanField("private")
    submit = SubmitField("Create Appointment")
