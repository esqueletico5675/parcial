from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum, auto

app = FastAPI()

# Clase principal
class Jugador(BaseModel):
    id: int
    nombre: str
    dorsal: int = 100
    edad: int
    altura: float
    equipo: str
    ataque: int = 50  # Para poder hacer la función de "batalla"
    vivo: bool = True  # Para simulaciones opcionales

    # Enum para posición en el campo
    class PosicionFutbol(Enum):
        Portero = auto()
        Defensa = auto()
        Mediocampista = auto()
        Delantero = auto()
        Extremo = auto()

# Instancias de jugadores
j1 = Jugador(id=1, nombre="Jose", dorsal=12, edad=15, altura=1.85, equipo="Sagitario", ataque=70)
j2 = Jugador(id=2, nombre="Sergio", dorsal=99, edad=16, altura=1.70, equipo="Cancer", ataque=80)
j3 = Jugador(id=3, nombre="Omar", dorsal=10, edad=17, altura=1.69, equipo="Leo", ataque=75)

# Lista de jugadores
lista_jugadores: list[Jugador] = [j1, j2, j3]

# Base de datos simulada
jugadores_db = [
    {"nombre": "Jose"},
    {"nombre": "Sergio"},
    {"nombre": "Omar"},
    {"nombre": "Leo"}
]


@app.get("/todos_los_jugadores/")
def mostrar_jugadores(skip: int = 0, limit: int = 3):
    return lista_jugadores[skip: skip + limit]


@app.get("/jugador_por_id/")
def mostrar_jugador(id: int = 0):
    for jugador in lista_jugadores:
        if jugador.id == id:
            return jugador
    return {"error": "jugador no encontrado"}


@app.get("/comparar_jugadores/")
def comparar_jugadores(jugador1_id: int = 0, jugador2_id: int = 0):
    jugador1 = None
    jugador2 = None

  
    for jugador in lista_jugadores:
        if jugador.id == jugador1_id:
            jugador1 = jugador
        elif jugador.id == jugador2_id:
            jugador2 = jugador


    if jugador1 is None or jugador2 is None:
        return {"error": "jugador no encontrado"}

  
    if jugador1.ataque > jugador2.ataque:
        return {"ganador": jugador1}
    elif jugador2.ataque > jugador1.ataque:
          return {"ganador": jugador2}
    else:
        return {"resultado": "empate"}


