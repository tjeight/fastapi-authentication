from pydantic import BaseModel



class UserCreate(BaseModel):
    user_name:str
    user_password:str




class UserReturn(BaseModel):
    user_name :str

    class config:
        orm_mode = True
