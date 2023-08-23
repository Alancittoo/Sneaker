from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class productForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    # image = FileField('Image', validators=[FileRequired(), FileAllowed()])
    description = StringField('Description', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()] )
    status = BooleanField('Status')
    price = IntegerField('Price', validators=[DataRequired()])


class productUpdateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    # image = FileField('Image', validators=[FileRequired(), FileAllowed()])
    description = StringField('Description', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()] )
    status = BooleanField('Status')
    price = IntegerField('Price', validators=[DataRequired()])
