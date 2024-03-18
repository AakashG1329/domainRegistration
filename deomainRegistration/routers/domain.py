from datetime import datetime
from typing import List
from fastapi import APIRouter, HTTPException,Depends,status
from pydantic import BaseModel
# from accountManagement.database import conn
from ..database import  engine,get_db
from .. import  models,schemas,oauth2
from sqlalchemy.orm import Session
router = APIRouter(
    tags=['Domain'],
    prefix='/domain'
)

models.Base.metadata.create_all(engine)
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

@router.get("/all",status_code=200,response_model=List[schemas.DomainResponceModel])
def get_all_domain(db: Session = Depends(get_db),current_user:schemas.Users=Depends(oauth2.get_current_user)):
    item =db.query(models.Domain).all()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Data Found")
    return item

@router.get("/{id}",status_code=200,response_model=schemas.DomainResponceModel)
def get_Domain(id:int,db: Session = Depends(get_db),current_user:schemas.Users=Depends(oauth2.get_current_user)):
    item =db.query(models.Domain).filter(models.Domain.id == id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} Data Not Found")
    return item
@router.post("/create",status_code=201)
def create_domain(request:schemas.Domain,db:Session=Depends(get_db),current_user:schemas.Users=Depends(oauth2.get_current_user)):
    create=models.Domain(domain_name=request.domain_name,registered_date=request.registered_date,expired_date=request.expired_date,created_date=datetime.now(),updated_date="")
    db.add(create)
    db.commit()
    db.refresh(create)
    return create

@router.put("/update/{id}",status_code=200)
async def update_Domain(id:int,request:schemas.DomainUpdateModel,db: Session = Depends(get_db),current_user:schemas.Users=Depends(oauth2.get_current_user)):
     
     
    domain= db.query(models.Domain).filter(models.Domain.id==id).first()
    if not domain:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} Data Not Found")
    domain.domain_name=request.domain_name
    domain.registered_date=request.registered_date 
    domain.registered_date=request.registered_date 
    domain.updated_date=datetime.now()
    
    db.commit()
    return "Updated successfully."
@router.delete("/delete/{id}",status_code=202)
def delete_domain(id:int,db: Session = Depends(get_db),current_user:schemas.Users=Depends(oauth2.get_current_user)):
    
    domain=db.query(models.Domain).filter(models.Domain.id == id)
    if not domain.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} Data Not Found")
    # print(Domain)
    # Domain.update(request)
    domain.delete(synchronize_session=False)
    db.commit()
    return "Deleted successfully."