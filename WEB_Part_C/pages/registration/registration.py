from flask import Blueprint, render_template
from flask import request, session, redirect, url_for
from db_connector import *


# registration blueprint definition
registration = Blueprint(
    'registration',
    __name__,
    static_folder='static',
    static_url_path='/registration',
    template_folder='templates'
)


# Routes
@registration.route('/registration', methods=['GET', 'POST'])
def index():
    session['existEmailAlert'] = False
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        birthdate = request.form['birthdate']
        password = request.form['password']

        # check if the user already registered with this email.
        customer = find_customer_by_email(email)
        # if the email already exist:
        if customer:
            session['existEmailAlert'] = True
            return render_template('registration.html')
        # if the email not exist -> create customer:
        else:
            new_customer = {
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'phone_number': phone_number,
                'birthdate': birthdate,
                'password': password
            }
            insert_customer(new_customer)
            massage = ('Your registration was successful! '
                       'Please proceed to sign in to your account')
        return render_template('logIn.html', massage=massage)
    # if method = GET:
    return render_template('registration.html')

