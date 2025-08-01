\
from fastapi import Response
from passlib.context import CryptContext





password_rules =  CryptContext(schemes="bcrypt",deprecated="auto")


def hash_password(password:str):
    return password_rules.hash(password)



def check_password(hashed_passowrd:str,password:str):
    return password_rules.verify(password,hashed_passowrd)





def set_cookie_token(response:Response,access_token:str):
    response.set_cookie(
        key = "access_token",
        value=access_token
        ,
        httponly=True,
        secure=True,
        samesite="lax"
    )