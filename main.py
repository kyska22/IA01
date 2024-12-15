from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def olamundo():
    return "Ola mundo"

@app.get("/rota1")
async def ondeestou():
    return "Voce esta na rota 1" 
