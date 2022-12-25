from fastapi import FastAPI
from models import Student
from schemas import User
import json

app = FastAPI()


# @app.post("/create")
# def createUser(name, age, dep,ids):
#     Student(u_id = ids, Name = name, Age = age, Dep = dep).save()
#     return {"Message ": f"{name} create successfully"}

@app.get("/alluser", tags=["User Crud"])
def getAllUser():
    return json.loads(Student.objects.to_json())

@app.get("/getuser/{id}", tags=["User Crud"])
def getUser(id: int):
    return json.loads(Student.objects(u_id = id).to_json())

@app.post("/create_user", tags=["User Crud"])
def create_user(usr: User):
    Student(u_id = usr.u_id, Name = usr.Name, Age = usr.Age, Dep = usr.Dep).save()
    return {"Message ": f"{usr.Name} create successfully"}

@app.delete("/delete_user/{id}", tags=["User Crud"])
def create_user(id):
    Student.objects(u_id = id).delete()
    return {"Message ": f"{id} delete successfully"}

@app.patch("/update_user", tags=["User Crud"])
def update_user(name: str, age: int):
    Student.objects.get(Name=name).update(Age=age)
    return json.loads(Student.objects.get(Name=name).to_json())