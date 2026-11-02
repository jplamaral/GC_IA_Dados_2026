from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

URL_FRUITYVICE = "https://www.fruityvice.com/api/fruit/"

sucos = []


class Suco(BaseModel):
    nome: str
    frutas: list[str]
    tem_gosto_de: str


class AtualizaSuco(BaseModel):
    frutas: list[str]


def buscar_fruta(nome):
    response = requests.get(URL_FRUITYVICE + nome)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail=f"Fruta '{nome}' não encontrada")

    dados = response.json()
    return {
        "nome": dados["name"],
        "calorias": dados["nutritions"]["calories"],
        "acucar": dados["nutritions"]["sugar"],
    }


def calcular_totais(frutas):
    calorias = 0
    acucar = 0
    for nome in frutas:
        fruta = buscar_fruta(nome)
        calorias += fruta["calorias"]
        acucar += fruta["acucar"]
    return round(calorias, 2), round(acucar, 2)


@app.get("/frutas/{nome}")
def consultar_fruta(nome: str):
    return buscar_fruta(nome)


@app.post("/sucos")
def cadastrar_suco(suco: Suco):
    calorias, acucar = calcular_totais(suco.frutas)
    novo_suco = {
        "id": len(sucos) + 1,
        "nome": suco.nome,
        "frutas": suco.frutas,
        "tem_gosto_de": suco.tem_gosto_de,
        "total_calorias": calorias,
        "total_acucar": acucar,
    }
    sucos.append(novo_suco)
    return novo_suco


@app.get("/sucos")
def listar_sucos():
    return sucos


@app.put("/sucos/{id}")
def atualizar_suco(id: int, dados: AtualizaSuco):
    for suco in sucos:
        if suco["id"] == id:
            calorias, acucar = calcular_totais(dados.frutas)
            suco["frutas"] = dados.frutas
            suco["total_calorias"] = calorias
            suco["total_acucar"] = acucar
            return suco
    raise HTTPException(status_code=404, detail="Suco não encontrado")