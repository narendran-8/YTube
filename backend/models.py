from mongoengine import connect, Document, StringField, DateTimeField
from datetime import datetime

connect("School")

class Student(Document):
    First_Name = StringField(required=True, max_length=30)
    Last_Name = StringField(required=True, max_length=30)
    Mail = StringField(required=True, max_length=50)
    password = StringField(required=True, min_length=3, max_length=150)
    crm_password = StringField(required=True, min_length=3, max_length=150)
    Date = DateTimeField(default=datetime.utcnow)
    
