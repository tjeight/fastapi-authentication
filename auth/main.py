from fastapi import FastAPI
from auth.routes import auth_router


# configure the app router
app = FastAPI()

app.include_router(auth_router)
