from datetime import timedelta
from fastapi import APIRouter,HTTPException,Depends
from db import get_db
from models import Users
from schemas import UserCreate, UserReturn
from sqlalchemy.orm import Session
from utils import hash_password,check_password, set_cookie_token
from auth import create_token
from fastapi.responses import JSONResponse


#create the router
router =  APIRouter()



@router.get("/")
def read_root():
    return {"meesage":"Welcome to the home Page"}




@router.post("/singup",response_model=UserReturn)
def create_user(user:UserCreate,db:Session =  Depends(get_db)):
    username   = user.user_name
    password  = user.user_password
    existing_user = db.query(Users).filter(Users.user_name == username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_password =  hash_password(password=password)
    new_user  = Users(user_name= username,user_password = hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/getuser/{user_id}",response_model=UserReturn)
def get_user(user_id:int,db:Session = Depends(get_db)):
    found_user =  db.query(Users).filter(Users.user_id == user_id).first()
    if not found_user:
        raise HTTPException(status_code=400,detail="User not found")
    
    return found_user

@router.post("/login")
def login_user(user:UserCreate,db:Session = Depends(get_db)):
    username  = user.user_name
    password = user.user_password

    found_user = db.query(Users).filter(Users.user_name == username).first()
    if not found_user:
        raise HTTPException(status_code=400,detail="User Not found")
    
    if not check_password(password=password,hashed_passowrd=found_user.user_password):
        raise HTTPException(status_code=400,detail="Wrong password entered")
    
    access_token = create_token({"sub":found_user.user_name},exp_time=timedelta(minutes=30))
    
    response = JSONResponse({"message":"User Login Successfully"})
    set_cookie_token(response,access_token)
    return response











