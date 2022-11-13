
from typing import Optional
from pydantic import BaseModel



class ClientModel(BaseModel):
   id :int 
   client_name :str
   post_url :str
   price :float
   days_number :int
   is_finished :bool 