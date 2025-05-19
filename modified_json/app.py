from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email
import json
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

CONFIG_FILE = 'config.json'

# Load config from file
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save config to file
def save_config(data):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# WTForm class
class ConfigForm(FlaskForm):
    site_name = StringField('Site Name', validators=[DataRequired()])
    admin_email = StringField('Admin Email', validators=[DataRequired(), Email()])
    maintenance_mode = SelectField('Maintenance Mode', choices=[('on', 'On'), ('off', 'Off')])
    submit = SubmitField('Save Changes')

# Route to display and process the form
@app.route('/', methods=['GET', 'POST'])
def config():
    config_data = load_config()
    form = ConfigForm(data=config_data)

    if form.validate_on_submit():
        updated_config = {
            "site_name": form.site_name.data,
            "admin_email": form.admin_email.data,
            "maintenance_mode": form.maintenance_mode.data
        }
        save_config(updated_config)
        flash('Configuration updated successfully!', 'success')
        return redirect(url_for('config'))

    return render_template('config_form.html', form=form)
    
if __name__ == '__main__':
    app.run(debug=True)
