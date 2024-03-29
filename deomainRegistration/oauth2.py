from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import FastAPI,Depends,HTTPException,status
from . import token 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

def get_current_user(data:str= Depends(oauth2_scheme)):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token.verifyToken(data,credentials_exception)
  