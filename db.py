from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from dotenv import load_dotenv
import os


load_dotenv()


DATABASE_URLS = os.getenv("DATABASE_URL") # type: ignore

Base =  declarative_base()



my_engine  = create_engine(DATABASE_URLS)


SessionLocal =  sessionmaker(bind=my_engine,autoflush=False,autocommit =False)


def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

