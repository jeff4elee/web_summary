from flask_wtf import FlaskForm
from wtforms import Form, StringField, BooleanField
from wtforms.validators import DataRequired

class URLForm(FlaskForm):

	url = StringField('url', validators=[DataRequired()])
	properties = ['p', 'div', 'td', 'body']