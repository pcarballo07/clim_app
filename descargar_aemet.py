# El siguiente script consulta los valores climatológicos diarios de estaciones reales de la Comunidad de Madrid durante 6 meses, 
# limpia los decimales con coma que devuelve AEMET (ej. "18,5" $\rightarrow$ 18.5), 
# convierte el viento de $\text{m/s}$ a $\text{km/h}$ ($\times 3.6$) y 
# guarda el resultado en data/clima_mock.json con los campos exactos del proyecto (fecha, zona, temperatura, humedad, viento, lluvia). 



import json #convierte los registros a formato JSON 
import os #permite crear carpetas del sistema
import time #sirve para trabajar con fechas
import requests #sirve para 

# Pega aquí tu API Key de AEMET OpenData
# Generada desde https://opendata.aemet.es/centrodedescargas/altaUsuario
API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJvbWJyYXZvQGljbG91ZC5jb20iLCJqdGkiOiI4MDFlM2E3Ny0wNGI0LTQ2MWMtOGMwMy1hMmIzYTc2ODQxZDYiLCJleHAiOjE4MDQyMzA4MzYsImlzcyI6IkFFTUVUIiwiaWF0IjoxNzk1NTkwODM2LCJ1c2VySWQiOiI4MDFlM2E3Ny0wNGI0LTQ2MWMtOGMwMy1hMmIzYTc2ODQxZDYiLCJyb2xlIjoiIn0.MYrcwbDnZTFBFrCX8xJWpo7bK8ORGksA7_SjM4w8dqc"

# Indicativos (IDEMA) reales de estaciones de AEMET en la Comunidad de Madrid
ESTACIONES_MADRID = {
    "Madrid Centro": "3195",        # Madrid, Retiro
    "Madrid Barajas": "3129",       # Madrid, Aeropuerto
    "Getafe": "3200",               # Getafe
    "Alcalá de Henares": "3170Y",   # Alcalá de Henares
    "Aranjuez": "3100B",            # Aranjuez
    "Colmenar Viejo": "3191E",      # Colmenar Viejo
    "Navacerrada": "2462",          # Puerto de Navacerrada
}


def limpiar_float(valor: str | None, defecto: float = 0.0) -> float:
    """Convierte cadenas numéricas de AEMET (con coma decimal) a float."""
    if not valor or valor in ("Ip", "Acum", "-"):
        return defecto
    try:
        return float(valor.replace(",", "."))
    except ValueError:
        return defecto


def obtener_datos_estacion(idema: str, fecha_ini: str, fecha_fin: str) -> list[dict]:
    """Realiza la doble petición exigida por la API de AEMET OpenData."""
    url = (
        f"https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/"
        f"datos/fechaini/{fecha_ini}T00:00:00UTC/fechafin/{fecha_fin}T23:59:59UTC/"
        f"estacion/{idema}"
    )
    headers = {"accept": "application/json", "api_key": API_KEY}

    # 1ª petición: obtener la URL temporal donde AEMET deja los datos
    resp_meta = requests.get(url, headers=headers, timeout=20)
    resp_meta.raise_for_status()
    meta = resp_meta.json()

    if meta.get("estado") != 200 or "datos" not in meta:
        print(f"Aviso en estación {idema}: {meta.get('descripcion', 'Sin datos')}")
        return []

    # 2ª petición: descargar el JSON real desde la URL proporcionada
    resp_datos = requests.get(meta["datos"], timeout=20)
    resp_datos.raise_for_status()
    return resp_datos.json()


def generar_mock_aemet(
    fecha_inicio: str = "2026-05-01",
    fecha_fin: str = "2026-10-31",
    ruta_salida: str = "data/clima_mock.json",
) -> None:
    registros_limpios = []

    for zona, idema in ESTACIONES_MADRID.items():
        print(f"Descargando datos reales de {zona} (estación {idema})...")
        datos_crudos = obtener_datos_estacion(idema, fecha_inicio, fecha_fin)

        for dia in datos_crudos:
            # AEMET usa 'tmax' (o 'tmed'), 'hrMedia', 'velmedia' (en m/s) y 'prec' (mm)
            if "tmax" not in dia or "hrMedia" not in dia:
                continue

            fecha = dia["fecha"]
            temperatura = round(limpiar_float(dia.get("tmax")), 1)
            humedad = int(round(limpiar_float(dia.get("hrMedia"), 50.0)))
            # Convertir velocidad del viento de m/s (AEMET) a km/h (proyecto)
            viento_kmh = round(limpiar_float(dia.get("velmedia")) * 3.6, 1)
            # 'Ip' en AEMET significa lluvia inapreciable (< 0.1 mm) -> 0.0
            lluvia = round(limpiar_float(dia.get("prec"), 0.0), 1)

            registros_limpios.append({
                "fecha": fecha,
                "zona": zona,
                "temperatura": temperatura,
                "humedad": max(0, min(100, humedad)),
                "viento": viento_kmh,
                "lluvia": max(0.0, lluvia),
            })

        # Pausa breve para respetar el límite de peticiones por minuto de AEMET
        time.sleep(1.5)

    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(registros_limpios, f, ensure_ascii=False, indent=2)

    print(f"\nProceso completado: {len(registros_limpios)} registros guardados en '{ruta_salida}'.")


if __name__ == "__main__":
    generar_mock_aemet()