from pydantic import BaseModel

class User(BaseModel):
    u_id: int
    Name: str
    Age: int
    Dep: str
