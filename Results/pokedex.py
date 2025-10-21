import pandas as pd
from datetime import datetime
import os

CSV_FILE = "C:\ProgramData\Jenkins\.jenkins\workspace\Pikapy\pokemon_del_dia.csv"

def mostrar_pokemon_del_dia():
    if not os.path.exists(CSV_FILE):
        print(f"❌ No se encontró el archivo {CSV_FILE}.")
        return

    try:
        # Leer CSV con pandas
        df = pd.read_csv(CSV_FILE)

        if df.empty:
            print("⚠️ El archivo CSV está vacío.")
            return

        # Tomar el último registro (el más reciente)
        ultimo = df.iloc[-1]
        print("──────────────────────────────")
        print(f"🔢 ID: {ultimo['numero']}")
        print(f"🐣 Nombre: {ultimo['nombre']}")
        print(f"💱 Tipo: {ultimo['tipos']}")
        print(f"👁️  Habilidades: {ultimo['habilidades']}")
        print("──────────────────────────────")

    except Exception as e:
        print(f"⚠️ Error al leer o procesar el archivo CSV: {e}")

print(f"📘 {datetime.now().strftime('%Y-%m-%d')}")
mostrar_pokemon_del_dia()
