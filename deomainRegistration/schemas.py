from datetime import datetime,date
from pydantic import BaseModel,validator
from typing import ClassVar, List,Optional

class Domain(BaseModel):
    domain_name:str
    registered_date:Optional[datetime] =None 
    expired_date:Optional[datetime] =None 
    # created_date:Optional[datetime] =None 
    # update_date:Optional[datetime] =None 

class DomainResponceModel(BaseModel):
    id:int
    domain_name:str
    registered_date:Optional[datetime] =None 
    expired_date:Optional[datetime] =None 
    created_date:Optional[datetime] =None 
    update_date:Optional[datetime] =None 
class DomainUpdateModel(BaseModel):
    domain_name:str
    registered_date:Optional[datetime] =None 
    expired_date:Optional[datetime] =None 
class Users(BaseModel):
    username:str
    password:str
    email_id:str
    # created_date:datetime
    # update_date:datetime
class UsersUpdateRequestModel(BaseModel):
    username:str
    email_id:str
class UserResponceModel(BaseModel):
    id:int
    username:str
    email_id:str
    created_date:Optional[datetime] =None 
    update_date:Optional[datetime] =None 

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email_id: Optional[str]=None