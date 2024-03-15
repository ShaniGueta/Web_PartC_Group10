import os
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# get your uri from .env file
uri = os.environ.get('DB_URI')

# create cluster
cluster = MongoClient(uri, server_api=ServerApi('1'))

# all dbs and collections that needed
clinicDB = cluster['clinicDB']
customersCOL = clinicDB['customers']
treatmentsCOL = clinicDB['treatments']
employeesCOL = clinicDB['employees']
appointmentsCOL = clinicDB['appointments']
registrationsCOL = clinicDB['registrations']


# all necessary functions
def find_customer_by_email(customer_email):
    return customersCOL.find_one({'email': customer_email})


def find_customer_by_email_password(customer_email, customer_password):
    return customersCOL.find_one({'email': customer_email, 'password': customer_password})


def insert_customer(customer_dict):
    customersCOL.insert_one(customer_dict)


def find_employee_by_phone_number(phone):
    return employeesCOL.find_one({'phoneNumber': phone})


def get_list_of_employees_by_role(role):
    return list(employeesCOL.find({'role': role}))


def get_list_of_scheduled_appointments_by_date(date):
    return list(registrationsCOL.find({'date': date}))


def insert_schedule_appointment(appointment_dict):
    return registrationsCOL.insert_one(appointment_dict)


def get_list_of_appointments_by_customer(customer_email):
    return list(registrationsCOL.find({'customer.email': customer_email}))
