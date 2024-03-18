from datetime import datetime
from typing import List
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from .. import  models,schemas,passwordHashing,token,oauth2
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException,Depends,status
from ..database import  engine,get_db

models.Base.metadata.create_all(engine)
router = APIRouter(
    tags=['User'],
    prefix='/user'
)

models.Base.metadata.create_all(engine)


@router.post("/login",status_code=200)
def user_login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(models.Users).filter(models.Users.email_id==request.username).first()
     
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials")
    if not passwordHashing.verify_password(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials")
    
    access_token = token.create_access_token(
        data={"sub": user.email_id} 
    )
    return {"email_id":user.email_id,"access_token":access_token, "token_type":"bearer"}


@router.get("/all",status_code=200,response_model=List[schemas.UserResponceModel])
def get_all_users(db: Session = Depends(get_db),current_user:schemas.Users=Depends(oauth2.get_current_user)):
    item =db.query(models.Users).all()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Data Found")
    return item

@router.get("/{id}",status_code=200,response_model=schemas.UserResponceModel)
def get_User(id:int,db: Session = Depends(get_db),current_user:schemas.Users=Depends(oauth2.get_current_user)):
    item =db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} Data Not Found")
    return item
@router.post("/create",status_code=201)
def create_users(request:schemas.Users,db:Session=Depends(get_db)):
    usernameValidate =db.query(models.Users).filter(models.Users.username== request.username).first()
    if usernameValidate:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{request.username} Username already Found")
    
    hashedPassword=passwordHashing.get_password_hash(request.password)
    create=models.Users( username=request.username,password=hashedPassword,email_id=request.email_id,created_date=datetime.now(),updated_date="")
    db.add(create)
    db.commit()
    db.refresh(create)
    return create

@router.put("/update/{id}",status_code=200)
async def update_Users(id:int,request:schemas.UsersUpdateRequestModel,db: Session = Depends(get_db),current_user:schemas.Users=Depends(oauth2.get_current_user)):
     
     
    users= db.query(models.Users).filter(models.Users.id==id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} Data Not Found")
    users.username=request.username
    users.email_id=request.email_id 
    users.updated_date=datetime.now() 
    db.commit()
    return "Updated successfully."
@router.delete("/delete/{id}",status_code=202)
def delete_users(id:int,db: Session = Depends(get_db),current_user:schemas.Users=Depends(oauth2.get_current_user)):
    
    Users=db.query(models.Users).filter(models.Users.id == id)
    if not Users.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} Data Not Found")
    Users.delete(synchronize_session=False)
    db.commit()
    return "Deleted successfully."