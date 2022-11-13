from database import sponsored 

def get_db():
   db = sponsored
   try:
      yield db
   finally:
      db.close() 