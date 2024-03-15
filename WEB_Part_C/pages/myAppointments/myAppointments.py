import datetime
from flask import Blueprint, render_template
from flask import Flask, redirect, url_for
from flask import request, session
from db_connector import *


# myAppointments blueprint definition
myAppointments = Blueprint(
    'myAppointments',
    __name__,
    static_folder='static',
    static_url_path='/myAppointments',
    template_folder='templates'
)


# Routes
@myAppointments.route('/myAppointments')
def index():
    # get all appointments history
    schedule_appointments_list = get_list_of_appointments_by_customer(session.get('email'))
    # sort by date
    schedule_appointments_list.sort(key=lambda x: x['date'], reverse=True)
    # today_date help control the availability of cancel buttons.
    # if the appointment date passed or  its today, the cancel button will not show
    today_date = datetime.date.today().strftime('%Y-%m-%d')
    return render_template('myAppointments.html',
                           schedule_appointments=schedule_appointments_list, today_date=today_date)


@myAppointments.route('/deleteAppointment', methods=['POST'])
def deleteAppointment():
    # get the appointment's details to delete it
    cancel_date = request.form['appo_date']
    cancel_time = request.form['appo_time']
    cancel_employee = find_employee_by_phone_number(request.form['appo_dentist_phone'])
    cancel_customer = find_customer_by_email(session.get('email'))
    # delete the appointment
    registrationsCOL.delete_one({
        'date': cancel_date,
        'time': cancel_time,
        'employee': cancel_employee,
        'customer': cancel_customer,
    })
    return redirect(url_for('myAppointments.index'))

