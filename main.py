from fastapi import FastAPI
from models import Student

app = FastAPI()

@app.get("/")
def index():
    return {"Massage":"Checking"}

@app.post("/create")
def createUser(name, age, dep):
    Student(Name = name, Age = age, Dep = dep).save()
    return {"Message ": f"{name} create successfully"}