from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class reviewForm(FlaskForm):
    comment = StringField('Comment', validators=[DataRequired()])
    stars = IntegerField('Price', validators=[DataRequired()])
    product_id = IntegerField('Product Id', validators=[DataRequired()])
    user_id = IntegerField('User Id', validators=[DataRequired()])


class reviewUpdateForm(FlaskForm):
    comment = StringField('Comment', validators=[DataRequired()])
    stars = IntegerField('Price', validators=[DataRequired()])
    product_id = IntegerField('Product Id', validators=[DataRequired()])
    user_id = IntegerField('User Id', validators=[DataRequired()])
