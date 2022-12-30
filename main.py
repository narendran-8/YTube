from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import json
#----------------------------------------------------
from models import Student
from schemas import User, UpdateUser
from logics import password_check, hash_password



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

@app.get("/get_user/{mail}", tags=["User"])
def getUser(mail: str):
    if Student.objects(Mail = mail):
        return json.loads(Student.objects(Mail = mail).to_json())
    else:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No user found...!")

@app.post("/create_user", tags=["User"])
def create_user(usr: User):
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
                password = hash_password(usr.password),
                crm_password = hash_password(usr.crm_password),
                ).save()

            return {"Message ": f"{usr.First_Name} {usr.Last_Name} create successfully"} 

    else:
        return {"Message ": "Password miss-match"}

@app.delete("/delete_user/{mail}", tags=["User"])
def create_user(mail):
    if Student.objects(Mail = mail):
        Student.objects(Mail = mail).delete()
        return {"Message ": f"{mail} delete successfully"}
    else:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No user found...!")

@app.put("/update_user", tags=["User"])
def update_user(mail: str, u_update: UpdateUser):
    try: 
        Student.objects.get(Mail=mail).update(
            First_Name = u_update.First_Name, 
            Last_Name = u_update.Last_Name,
            password = u_update.password,
            crm_password = u_update.crm_password,
        )
    except Exception:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No user found...!")
    return {"Message ": f"{u_update.First_Name} {u_update.Last_Name} update successfully"}