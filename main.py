from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import json
#----------------------------------------------------
from models import Student
from schemas import User
from logics import password_check



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/all_user", tags=["User"])
def getAllUser():
    return json.loads(Student.objects.to_json())

@app.get("/get_user/{id}", tags=["User"])
def getUser(id: int):
    return json.loads(Student.objects(u_id = id).to_json())

@app.post("/create_user", tags=["User"])
def create_user(usr: User):
    now = datetime.now()
    if password_check(usr.password, usr.crm_password):
        if Student.objects(Mail = usr.Mail):
            print("User already found...!")
            return {"Message ": f"{usr.First_Name} {usr.Last_Name} User already found...!"}
        else:
            print("not found...!")
            Student(
                First_Name = usr.First_Name, 
                Last_Name = usr.Last_Name,
                Mail = usr.Mail,
                password = usr.password,
                crm_password = usr.crm_password,
                Date = now.strftime("%d-%m-%Y, %H:%M:%S")
                ).save()

            return {"Message ": f"{usr.First_Name} {usr.Last_Name} create successfully"} 

    else:
        return {"Message ": "Password miss-match"}

@app.delete("/delete_user/{id}", tags=["User"])
def create_user(id):
    Student.objects(u_id = id).delete()
    return {"Message ": f"{id} delete successfully"}

@app.patch("/update_user", tags=["User"])
def update_user(name: str, age: int): 
    Student.objects.get(Name=name).update(Age=age)
    return json.loads(Student.objects.get(Name=name).to_json())