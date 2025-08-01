from jose import JWTError,jwt
from datetime import datetime,timedelta,timezone
from dotenv import load_dotenv
import os
load_dotenv()



def create_token(data:dict,exp_time:timedelta = None):
    copied_data = data.copy()
    expire_time =  datetime.now(timezone.utc)+(exp_time or timedelta(minutes=15))
    copied_data.update({'exp_time':int(expire_time.timestamp())})
    return jwt.encode(copied_data,os.getenv("SECRET_KEY"),os.getenv("ALGORITHM"))

