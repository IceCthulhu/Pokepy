import requests
import pandas as pd

def obtener_datos_pokemon(nombre):
    #Extrae datos del Pokémon desde la API
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    respuesta = requests.get(url)
    
    if respuesta.status_code != 200:
        print(" No se pudo obtener datos para "+nombre)
        return None
    
    datos = respuesta.json()
    info = {
        "nombre": datos["name"],
        "altura": datos["height"],
        "peso": datos["weight"],
        "tipo": [t["type"]["name"] for t in datos["types"]],
        "habilidades": [a["ability"]["name"] for a in datos["abilities"]]
    }
    return info

def ejecutar_etl(lista_pokemon):
    #ETL a CSV
    resultados = []
    for nombre in lista_pokemon:
        info = obtener_datos_pokemon(nombre)
        if info:
            resultados.append(info)
    
    df = pd.DataFrame(resultados)
    df.to_csv("pokemon_data.csv", index=False)
    print("✅ Datos guardados en pokemon_data.csv")

lista = ["pikachu", "bulbasaur", "charmander", "squirtle", "mew"]
ejecutar_etl(lista)
