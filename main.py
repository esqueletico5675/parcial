from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum,auto

app = FastAPI()

class Caballero(BaseModel):
    id:int
    name:str
    vida:int = 100
    ataque:int
    vivo:bool = True
    material = Enum
    constelacion:str 
    

    class material (Enum):
        oro = auto()
        plata = auto()
        bronce = auto()


p1 =Caballero(id=1,name="jose",vida=100,ataque=15,vivo=True,constelacion= "sagitario")
p2 =Caballero(id=2,name="sergio",vida=100,ataque=16,vivo=True, constelacion= "cancer")
p3= Caballero(id=3,name="omar",vida=100,ataque=15,vivo=True,constelacion= "leo")

new_caballero:list[Caballero] =[p1,p2,p3]

Caballero_db = [
    {"name": "jose"},
    {"name": "sergio"},
    {"name": "omar"},
    {"name": "leo"}
    
]

@app.get("/allcaballeros/")
def show_All_Caballero(skip: int=0, limit:int=3):
    return new_caballero[skip: skip+limit]

@app.get("/solo_caballero_por_id")
def show_one_pokemon(pos:int=0):
    for caballerito in new_caballero:
        if (caballerito.id==pos):
            return caballerito
        else:
            return{"caballero no encontrado"}


@app.get("/fight_caballero/")
def battle(caballero1: int=0, caballero2:int=0):

    eleccion1 = None
    eleccion2 = None

    for caballerito in new_caballero:
        if caballerito.id == caballero1:
            eleccion1 = caballerito
        elif caballerito.id == caballero2:
            eleccion2 = caballerito

   
    if eleccion1 is None or eleccion2 is None:
        return {"error": "caballero no encontrado"}

    if eleccion1.ataque < eleccion2.ataque:
        return {"el ganador es": eleccion2}

    elif eleccion2.ataque < eleccion1.ataque:
        return {"el ganador es": eleccion1}

    else:
        return {"resultado": "empate"}

