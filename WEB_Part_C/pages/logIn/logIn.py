from flask import Blueprint, render_template
from flask import request, session, redirect, url_for
from db_connector import *

# about blueprint definition
logIn = Blueprint(
    'logIn',
    __name__,
    static_folder='static',
    static_url_path='/logIn',
    template_folder='templates'
)


# Routes
@logIn.route('/')
def redirect_login():
    if session.get('logged_in'):
        return redirect(url_for('makeAnAppointment.index'))
    return redirect(url_for('logIn.index'))


@logIn.route('/logIn', methods=['GET', 'POST'])
def index():
    # if method == POST:
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # check with DB if this user exist
        customer = find_customer_by_email_password(email, password)
        # if user exist:
        if customer:
            session['logged_in'] = True
            session['email'] = customer['email']
            session['userName'] = customer['first_name'].title()
            return redirect(url_for('makeAnAppointment.index'))
        # if user dont exist
        else:
            customer = find_customer_by_email(email)
            # if email exist -> wrong password
            if customer:
                massage = 'Wrong password, try again'
                return render_template('logIn.html', massage=massage)
            # if email dont exist -> wrong email
            else:
                massage = 'Wrong email, try again'
                return render_template('logIn.html', massage=massage)
    # if method == GET:
    return render_template('logIn.html')


@logIn.route('/logout')
def logout():
    session.clear()
    session['logged_in'] = False
    print(session)
    return redirect(url_for('logIn.index'))
