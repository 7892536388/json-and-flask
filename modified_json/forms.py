from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class ConfigForm(FlaskForm):
    site_name = StringField('Site Name', validators=[DataRequired()])
    admin_email = StringField('Admin Email', validators=[DataRequired(), Email()])
    maintenance_mode = SelectField('Maintenance Mode', choices=[('on', 'On'), ('off', 'Off')])
    submit = SubmitField('Save Changes')
