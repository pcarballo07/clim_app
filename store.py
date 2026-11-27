import json
import os

path_file = "data/mock_real.json"

def download(path: str = path_file) -> list:
    """Lee el archivo JSON y devuelve una lista de diccionarios."""
    # 1. Si el archivo no existe, devolvemos una lista vacía para evitar errores
    if not os.path.exists(path):
        print(f"❌ No encuentro el archivo. Python busca en: {os.path.abspath(path)}")
        return []
    
    try:
        with open(path, "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
            print(f"✅ Archivo {path} cargado correctamente.")
            return data
    except json.JSONDecodeError:
        # Si el archivo está vacío o corrupto, devolvemos lista vacía
        return []


def save_data(datos: list, path: str) -> None:
    """Guarda la lista actualizada en el JSON."""
    with open(path, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)