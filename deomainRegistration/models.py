from datetime import datetime
from sqlalchemy import Column,Integer,String,Float,DateTime

from .database import Base

class Domain(Base):
    __tablename__="tbl_domain"
    id= Column(Integer, primary_key=True, index=True)
    domain_name=Column(String(250))
    registered_date=Column(DateTime,nullable=True)
    expired_date=Column(DateTime,nullable=True)
    created_date=Column(DateTime,nullable=True)
    update_date=Column(DateTime,nullable=True)
   
class Users(Base):
    __tablename__="tbl_users"
    id= Column(Integer, primary_key=True, index=True)
    username=Column(String(250))
    password=Column(String(250))
    email_id=Column(String(250))
    created_date=Column(DateTime,nullable=True)
    update_date=Column(DateTime,nullable=True)
   

