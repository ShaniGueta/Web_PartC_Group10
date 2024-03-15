from flask import Blueprint, render_template
from flask import Flask, redirect, url_for
from flask import request, session
from db_connector import *
import datetime

# blueprint definition
makeAnAppointment = Blueprint(
    'makeAnAppointment',
    __name__,
    static_folder='static',
    static_url_path='/makeAnAppointment',
    template_folder='templates'
)


def listOpenAppointments(date):
    # get list of all appointments scheduled in the specific date
    scheduled_appointments = get_list_of_scheduled_appointments_by_date(date)
    # open empty list of available appointment to register
    open_appointments = []
    # create list of all work's hours
    time = ['{:02d}:00'.format(hour) for hour in range(8, 20)] + ['{:02d}:30'.format(hour) for hour in range(8, 20)]
    # create list of employees according to treatment type - if doctor or just dentist
    if session.get('treatment') == 'Dental_cleanings':
        # only dentist do dental cleaning (not doctors)
        # employees will be all dentists (not Dr) in the clinic
        employees = get_list_of_employees_by_role('Dentist')
    else:
        # other treatments are done by doctors
        # employees will be all doctors (not dentist) in the clinic
        employees = get_list_of_employees_by_role('Doctor')

    # create list of all potential appointments for this date
    for t in time:
        for employee in employees:
            open_appointments.append({'date': date, 'time': t, 'dentist': employee})

    # remove all scheduled-appointments taken by other customers from the open_appointments list
    for appointment in open_appointments[:]:
        for sch_appointment in scheduled_appointments:
            if appointment['time'] == sch_appointment['time'] and appointment['dentist'] == sch_appointment['employee']:
                open_appointments.remove(appointment)
                break

    # return list of only available appointments for the specific given date ordered by time
    return sorted(open_appointments, key=lambda x: x['time'])


# Routes
@makeAnAppointment.route('/makeAnAppointment')
def index():
    session['show_open_appointments_table'] = False
    customer = find_customer_by_email(session.get('email'))
    userName = customer['first_name'].title()
    return render_template('makeAnAppointment.html', userName=userName)


@makeAnAppointment.route('/findAnAppointment')
def findAnAppointment():
    session['treatment'] = request.args['treatmentType']
    session['date'] = request.args['dateAppointment']
    open_appointments = listOpenAppointments(session.get('date'))
    session['show_open_appointments_table'] = True
    return render_template('makeAnAppointment.html', open_appointments=open_appointments)


@makeAnAppointment.route('/insertAppointment', methods=['POST'])
def insertAppointment():
    chosen_time = request.form['chosen_time']
    chosen_date = request.form['chosen_date']
    chosen_treatment = session.get('treatment')
    dentist_phone = request.form['chosen_dentist_phone']
    chosen_dentist = find_employee_by_phone_number(dentist_phone)
    appo_customer = find_customer_by_email(session.get('email'))

    # check if exist another appointment in the same date and time
    myquery = {"date": chosen_date, "time": chosen_time, 'customer.email': session.get('email')}
    scheduled_appointment_same_dt = list(registrationsCOL.find(myquery))
    # if not exist -> schedule it. insert to registration collection
    if not scheduled_appointment_same_dt:
        appointment = {
            'date': chosen_date,
            'time': chosen_time,
            'employee': chosen_dentist,
            'treatment': chosen_treatment,
            'customer': appo_customer,
        }
        insert_schedule_appointment(appointment)
        return redirect(url_for('myAppointments.index'))
    else:
        massage = "Sorry, you already have an appointment for that date and time as you can see here:"
        today_date = datetime.date.today().strftime('%Y-%m-%d')
        return render_template('myAppointments.html',
                               massage=massage,
                               schedule_appointments=scheduled_appointment_same_dt,
                               today_date=today_date)
