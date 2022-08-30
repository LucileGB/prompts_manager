from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp, ValidationError


class TagsetURL(Regexp):
    def __init__(self, message=None):
        super().__init__("https://archiveofourown.org/tag_sets/", message=message)

    def __call__(self, form, field):
        message = self.message
        if message is None:
            message = "This is not a proper AO3 tagset URL." #if this doesn't work : = field.gettext("...")
        super().__call__(form, field, message)


class TagsetForm(FlaskForm):
    url = StringField("Tagset URL", validators=[DataRequired(), TagsetURL()])
    submit = SubmitField("Submit")


class PromptForm(FlaskForm):
    prompt = TextAreaField("Tagset URL", validators=[DataRequired(), Length(max=200)])
    submit = SubmitField("Submit")
