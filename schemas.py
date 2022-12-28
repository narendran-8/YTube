from pydantic import BaseModel

class User(BaseModel):
    First_Name: str
    Last_Name: str
    Mail: str
    password: str
    crm_password: str

class UpdateUser(User):
    pass