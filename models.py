from db import Base
from sqlalchemy import Column,Integer,String




#this models are the mapping to the table in the sql
class Users(Base):
    __tablename__ = "usersdemo"
    user_id = Column(Integer,primary_key=True,index=True)
    user_name = Column(String,unique=True)
    user_password = Column(String)