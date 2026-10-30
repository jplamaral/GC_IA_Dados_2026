from fastapi import FastAPI, HTTPException
import requests
app = FastAPI();

URL_FRUITYVICE = "https://fruityvice.com/api/fruit/"

@app.get("/frutas/{nomes}")
def get_fruit_info(nomes: str):
    return {"fruta": nomes, }
    
