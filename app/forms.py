from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

class NewNailsForm(FlaskForm):
    title = StringField("Nails title", validators=[DataRequired()])
    description = StringField("Nails Description")
    price = StringField("Nails Price", validators=[DataRequired()])
    service_type = SelectField("service_type", choices=[('Manicure'), ('Pedicure')],validators=[DataRequired()])
    submit = SubmitField('Submit')
