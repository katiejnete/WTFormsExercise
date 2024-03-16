"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField(
        "Pet Name", validators=[DataRequired(message="Please enter non-blank name.")]
    )
    species = SelectField(
        "Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")]
    )
    photo_url = StringField(
        "Photo URL", validators=[Optional(), URL(message="Please enter valid URL.")]
    )
    age = FloatField(
        "Age",
        validators=[
            Optional(),
            NumberRange(min=0, max=30, message="Please enter age between 0 and 30."),
        ],
    )
    notes = TextAreaField("Notes", validators=[Optional()])
    submit = SubmitField("Add Pet")
