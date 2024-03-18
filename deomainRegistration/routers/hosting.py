from datetime import datetime
from typing import List
from fastapi import APIRouter, HTTPException,Depends,status
from pydantic import BaseModel
# from accountManagement.database import conn
from ..database import  engine,get_db
from .. import  models,schemas,oauth2
from sqlalchemy.orm import Session
router = APIRouter(
    tags=['Hosting'],
    prefix='/hosting'
)

models.Base.metadata.create_all(engine)
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

@router.get("/all",status_code=200,response_model=List[schemas.HostingResponceModel])
def get_all_hosting(db: Session = Depends(get_db),current_user:schemas.Users=Depends(oauth2.get_current_user)):
    item =db.query(models.Hosting).all()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Data Found")
    return item

@router.get("/{id}",status_code=200,response_model=schemas.HostingResponceModel)
def get_hosting(id:int,db: Session = Depends(get_db),current_user:schemas.Users=Depends(oauth2.get_current_user)):
    item =db.query(models.Hosting).filter(models.Hosting.id == id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} Data Not Found")
    return item
@router.post("/create",status_code=201)
def create_hosting(request:schemas.Hosting,db:Session=Depends(get_db),current_user:schemas.Users=Depends(oauth2.get_current_user)):
    create=models.Hosting(hosting_server_type=request.hosting_server_type,registered_date=request.registered_date,expired_date=request.expired_date,email_id=request.email_id,mobile_no=request.mobile_no,created_date=datetime.now(),updated_date="")
    db.add(create)
    db.commit()
    db.refresh(create)
    return create

@router.put("/update/{id}",status_code=200)
async def update_hosting(id:int,request:schemas.Hosting,db: Session = Depends(get_db),current_user:schemas.Users=Depends(oauth2.get_current_user)):
     
     
    hosting= db.query(models.Hosting).filter(models.Hosting.id==id).first()
    if not hosting:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} Data Not Found")
    hosting.hosting_server_type=request.hosting_server_type
    hosting.registered_date=request.registered_date 
    hosting.email_id=request.email_id 
    hosting.mobile_no=request.mobile_no 
    hosting.expried_date=request.expired_date 
    hosting.updated_date=datetime.now()
    
    db.commit()
    return "Updated successfully."
@router.delete("/delete/{id}",status_code=202)
def delete_hosting(id:int,db: Session = Depends(get_db),current_user:schemas.Users=Depends(oauth2.get_current_user)):
    
    hosting=db.query(models.Hosting).filter(models.Hosting.id == id)
    if not hosting.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} Data Not Found")
    # print(hosting)
    # hosting.update(request)
    hosting.delete(synchronize_session=False)
    db.commit()
    return "Deleted successfully."