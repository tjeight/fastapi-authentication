from fastapi import FastAPI
from routes import router
from db import Base,my_engine






app =  FastAPI()
Base.metadata.create_all(my_engine)
app.include_router(router=router)