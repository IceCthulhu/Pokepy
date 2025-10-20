import requests
import datetime
import pandas as pd

def obtener_pokemon(numero):
    url = f"https://pokeapi.co/api/v2/pokemon/{numero}"
    r = requests.get(url)
    if r.status_code != 200:
        print(f"⚠️ No se pudo obtener el Pokémon #{numero}")
        return None

    data = r.json()
    info = {
        "numero": numero,
        "nombre": data["name"].capitalize(),
        "altura": data["height"],
        "peso": data["weight"],
        "tipos": [t["type"]["name"] for t in data["types"]],
        "habilidades": [a["ability"]["name"] for a in data["abilities"]],
    }
    return info


def obtener_numero_pokemon(fecha_inicio=datetime.date(2025, 1, 20)):
    """Calcula el número del Pokémon según los días transcurridos"""
    hoy = datetime.date.today()
    delta_dias = (hoy - fecha_inicio).days
    numero_pokemon = (delta_dias % 898) + 1  # 898 = total actual de Pokémon
    return numero_pokemon


def pokedeldia():
    numero = obtener_numero_pokemon()
    print(f"📅 Hoy corresponde al Pokémon #{numero}")
    pokemon = obtener_pokemon(numero)

    if pokemon:
        df = pd.DataFrame([pokemon])
        df.to_csv("pokemon_del_dia.csv", index=False)
        print(f"✅ Pokémon del día guardado: {pokemon['nombre']}")
        print(df)


pokedeldia()
