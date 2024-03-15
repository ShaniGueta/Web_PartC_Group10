from flask import Flask

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## registration
from pages.registration.registration import registration
app.register_blueprint(registration)

## logIn
from pages.logIn.logIn import logIn
app.register_blueprint(logIn)

## makeAnAppointment
from pages.makeAnAppointment.makeAnAppointment import makeAnAppointment
app.register_blueprint(makeAnAppointment)

## myAppointments
from pages.myAppointments.myAppointments import myAppointments
app.register_blueprint(myAppointments)


###### Components
## header
from components.header.header import header
app.register_blueprint(header)

## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)









