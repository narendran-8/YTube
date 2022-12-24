from mongoengine import connect, Document, StringField, IntField

connect("School")

class Student(Document):
    Name = StringField()
    Age = IntField()
    Dep = StringField()
