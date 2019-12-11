#============================================
# Title: Assignment 9.3
# Author: Justin Singleton
# Date: 11 December 2019
# Description: This program demonstrates the
# use of Python for updating and deleting.
#============================================

from pymongo import MongoClient
import pprint
import datetime

client = MongoClient("localhost", 27017)

db = client.web335

db.users.update_one(
    {'employee_id': "0000008"},

    {
        "$set": {
            "email": "jsingleton@my365.bellevue.edu"
        }
    }
)

pprint.pprint(db.users.find_one({"employee_id": "0000008"}))