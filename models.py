from mongoengine import connect, Document, StringField, IntField

connect("School")

class Student(Document):
    u_id = IntField(required=True)
    Name = StringField(required=True, min_length=3, max_length=30)
    Age = IntField(required=True)
    Dep = StringField(required=True, max_length=5)
