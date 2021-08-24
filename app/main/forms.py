from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

################
# Custom Forms #
################
#
# an example of how to use Flask_wtf to create custom forms which you can send
# to your templating engine (jinja) to render

class LandingPageForm(FlaskForm):
    word_one = StringField('The first word', validators=[DataRequired()])
    word_two = StringField('The second word', validators=[Length(min=0, \
                                                            max=3000)])
    submit = SubmitField('Submit')


