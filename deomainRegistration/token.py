from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from .schemas import TokenData


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30





def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    token=encoded_jwt.replace(".","")
    return token


def verifyToken(token:str,credentials_exception):
     try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
       
        email_id: str = payload.get("sub")
        if email_id is None:
            raise credentials_exception
        token_data = TokenData(email_id=email_id)
     except JWTError:
        return 