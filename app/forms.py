from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp


class TagsetURL(Regexp):
    def __init__(self, message=None):
        super().__init__(
            "https://archiveofourown.org/tag_sets/",
            message=message
            )

    def __call__(self, form, field):
        message = self.message
        if message is None:
            # For cases where field.gettext("...") doesn't work
            message = "This is not a proper AO3 tagset URL."
        super().__call__(form, field, message)


class TagsetForm(FlaskForm):
    url = StringField(
        "Tagset URL",
        validators=[DataRequired(), TagsetURL()]
        )
    submit = SubmitField("Submit")


class PromptForm(FlaskForm):
    prompt = TextAreaField(
        "Prompt",
        validators=[DataRequired(), Length(max=500)]
        )
    submit = SubmitField("Submit")


class EditPromptForm(FlaskForm):
    id = StringField("Id", validators=[DataRequired(), ])
    body = TextAreaField(
        "Prompt",
        validators=[DataRequired(), Length(max=500)]
        )
    submit = SubmitField("Submit")
