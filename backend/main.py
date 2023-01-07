from fastapi import FastAPI, HTTPException, status, Depends, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import json
#----------------------------------------------------
from models import Student, ImageStore
from schemas import User, UpdateUser, UrlBody
from logics import password_check, hash_password, yt_link_gen
from download import YTDownload

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

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
def create_user(user: User, my_file: UploadFile = File(...)):
    if password_check(user.password, user.crm_password):
        if Student.objects(Mail = user.Mail):
            print("User already found...!")
            return {"Message ": f"{user.First_Name} {user.Last_Name} User already found...!"}
        else:
            print("not found...!")
            Student(
                Profile_pic = my_file.filename,
                First_Name = user.First_Name, 
                Last_Name = user.Last_Name,
                Mail = user.Mail,
                password = hash_password(user.password),
                crm_password = hash_password(user.crm_password),
                ).save()

            return {"Message ": f"{user.First_Name} {user.Last_Name} create successfully"} 

    else:
        return {"Message ": "Password miss-match"}

@app.delete("/delete_user/{mail}", tags=["User"])
def delete_user(mail):
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

@app.post("/token", tags=["login"])
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    
    print(username, password)

@app.get("/", tags=["login"])
def index(token: str = Depends(oauth2_schema)):
    return {"message":"hello world!!!"}


@app.post("/down")
def downLoad(url: UrlBody):
    return yt_link_gen(url.Source_url)


@app.post("/image_upload")
def image_upload(my_file: UploadFile = File(...)):
    ImageStore(
       ImageName = my_file.filename ,
        SaveImage = my_file.file
    ).save()
    return {"File_name": my_file.filename, "File":my_file.file, "message":"Store successfully"}

@app.get("/get_upload")
def get_image():
    return {"message":"Store successfully"}