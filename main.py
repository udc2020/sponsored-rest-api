from fastapi import FastAPI
from routers import clients_router 

app = FastAPI() 



app.include_router(clients_router.router)

