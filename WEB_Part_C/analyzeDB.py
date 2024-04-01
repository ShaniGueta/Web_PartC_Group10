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


def analyzeDB():
    customers = list(customersCOL.find())
    print(customers)

    treatments = list(treatmentsCOL.find())
    print(treatments)

    employees = list(employeesCOL.find())
    print(employees)

    appointments = list(appointmentsCOL.find())
    print(appointments)

    registrations = list(registrationsCOL.find())
    print(registrations)

