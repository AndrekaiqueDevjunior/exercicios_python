from fastapi import FastAPI, HTTPException
from app.routers.vendas import router

### da pasta principal APP
### da pasta routers sub-pasta de APP /\
### vendas.py da pasta routers
### import router



#from asyncio
# io = entrada e saida
app = FastAPI() # app recebe a  FASTAPI 

app.include_router(router)