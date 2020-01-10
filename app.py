from flask import Flask, render_template, request, jsonify, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired, Email
from wtforms import SelectField, SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap
#from contact import ContForm
from survey import Form
from flask import send_file
from flask_mail import Mail, Message as mMail
import os
import urllib.parse
#from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SECRET_KEY'] = 'oratoroeuaroupadoreideroma123'
app.config['DEBUG'] = True
app.config['MAIL_USERNAME'] = 'irishousingproject@gmail.com'
app.config['MAIL_SERVER']: 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'irishousingproject@gmail.com',
app.config['MAIL_PASSWORD'] = 'irish_housingProject19'
app.config['Mail_DEFAULT_SENDER'] = 'default_sender_email'

#app.config.update(mail_settings)



# extensions
#db = SQLAlchemy(app)
mail = Mail(app)
mail.init_app(app)
Bootstrap(app)


class ContForm(Form):
    name = TextField("Name", [DataRequired()])
    email = StringField('Email address', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    subject = TextField("Subject", [DataRequired()])
    message = TextAreaField("Message", [DataRequired()])
    submit = SubmitField("Send")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()

    if request.method == 'POST':
        if form.validate_on_submit():
            details = request.form
            Emal = form.Email, sex = form.sex, age = form.age,
            Marital = form.Marital, county = form.county,
            Property = form.Property, PropertyStatus = form.PropertyStatus,
            AmountPaid = form.AmountPaid, Rooms = form.Rooms,
            People = form.People
            db("INSERT INTO survey(Email, sex, age, Marital, county, Property, PropertyStatus, AmountPaid, Rooms, People) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
               (Email, sex, age, Marital, county, Property, PropertyStatus, AmountPaid, Rooms, People))
            # db.connection.commit()
            #cursor = db.cursor()

            # db.close()
            flash(u'Something went wrong!', 'success')

        else:
            flash(u'Thank you for your collaboration!', 'error')
        return redirect(url_for('index'))
    return render_template('index1.html', form=form)


@app.route('/About', methods=['GET', 'POST'])
def About():
    return render_template('About1.html')


@app.route('/Design', methods=['GET', 'POST'])
def Design():
    return render_template('Design.html')


@app.route('/Contact', methods=['GET', 'POST'])
def Contact():
    form = ContForm()
    if request.method == 'POST':
        if form.validate() == True:
            flash('All fields are required.')
            return render_template('Contact.html', form=form)
        else:
            msg = mMail(subject=form.subject,
                          sender=form.email, recipients=['reciever_mail_id'],
                          body=form.message)
            msg.body = form.message
            #
            #with app.app_context():
            mail.send(msg)
            #msg.body = "%s %s"
            flash('not sure what to write here just yet')
            return render_template('Contact.html', form=form, success=True)

        return render_template('Contact.html', success=True)

    elif request.method == 'GET':
        return render_template('Contact.html', form=form)


@app.route('/file-downloads/')
def file_downloads():
    try:
        return render_template('downloads.html')
    except Exception as e:
        return str(e)


@app.route('/return-files/')
def return_files():
    try:
        
        return send_file('C:/Users/rapha/Documents/College/appProject/static/toDownload/project.pdf', attachment_filename='project.pdf')
    except Exception as e:
        return str(e)


@app.route('/return-files1/')
def return_files1():
    try:
        return redirect('https://github.com/Reinhold83/appProject.git')
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)
