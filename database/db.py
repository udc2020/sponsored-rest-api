from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base , sessionmaker
from sqlalchemy import Column, Boolean, Integer, String ,Float

import os

class Db :
   base = declarative_base()
   BASE_DIR = os.path.dirname('./')
   connect = "sqlite:///" +os.path.join(BASE_DIR,'sponsored.sqlite')
   engin = None
   Session = sessionmaker()
   
   def connect_db (self):
      self.engin = create_engine(self.connect,echo=True)
      self.base.metadata.create_all(self.engin)
      
   def instence_db (self):
      return self.Session(bind=self.engin)
   
   
   
   
class Client (Db.base):
    __tablename__ = "client"
    
    id = Column(Integer,primary_key=True,index=True)
    client_name = Column(String(255),nullable=False)
    post_url = Column(String,nullable=False)
    price =  Column(Float,nullable=False)
    days_number = Column(Integer,nullable=False)
    is_finished = Column(Boolean,nullable=False)       



db  = Db()
connect = db.connect_db()
sponsored = db.instence_db()