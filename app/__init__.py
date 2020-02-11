from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ramdeenmonelal'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = 
app.config['MAIL_PASSWORD'] = 

mail = Mail(app)

"""from app import viewsfrom flask import Flask

app = Flask(__name__)"""
from app import views