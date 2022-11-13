from fastapi import FastAPI , Depends ,status ,Response ,HTTPException , APIRouter
from schemas.cleint_model import *
from typing import Optional

from sqlalchemy.orm import Session

from database import Client

 
from dependencies import get_db


router = APIRouter()


@router.get('/api/clients',tags=["Clients"])
def get_client_all(db : Session = Depends(get_db)):
   return db.query(Client).all()





@router.get('/api/client/{id}' ,status_code=status.HTTP_200_OK ,tags=["Clients"])
def get_client(id :int , res :Response, db : Session = Depends(get_db)):
   client = db.query(Client).filter(Client.id == id).first()
   if not client : 
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=f"we not found client id :{id}") 
      #  res.status_code = status.HTTP_404_NOT_FOUND
      #  return {"client":f"we not found client id :{id}"}
   return client


@router.delete('/api/client/{id}' ,status_code=status.HTTP_204_NO_CONTENT)
def remove_client(id :int , res :Response, db : Session = Depends(get_db)):
   client = db.query(Client).filter(Client.id == id)
   if not client.first():
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Not found id:{id}")
   client.delete()
   db.commit()

   return {"msg":"Done!"}





@router.post('/api/client' ,status_code=status.HTTP_201_CREATED)
def new_client(client :ClientModel ,db : Session = Depends(get_db)):
   new_cleint = Client(id=client.id,client_name=client.client_name,post_url=client.post_url,price=client.price,days_number=client.days_number,is_finished=client.is_finished)
   db.add(new_cleint)
   db.commit()
   db.refresh(new_cleint)
   return client


@router.put('/api/client/{id}' ,status_code=status.HTTP_202_ACCEPTED)
def new_client(id :int ,client :ClientModel ,db : Session = Depends(get_db)):
   old_client = db.query(Client).filter(Client.id == id)
   
   if not old_client.first():
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Not found id:{id}")
   
   old_client.update({
      Client.client_name:client.client_name,
      Client.price:client.price,
      })
   
   
   db.commit()
   
   return client

