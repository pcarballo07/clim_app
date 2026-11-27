# Importamos las funciones de lectura y escritura desde el módulo store.py
from store import download, save_data
# Importamos las funciones de validación y comprobación de duplicados desde validations.py
from validations import (
    is_duplicate,
    get_valid_zone,
    get_valid_temperature,
    get_valid_humidity,
    get_valid_wind,
    get_valid_rain
)
# Importamos la clase date del módulo nativo datetime para obtener la fecha actual
from datetime import date

path_file = "data/mock_real.json"

# Definimos la función principal para registrar una nueva medición climática
def register():
    # Imprimimos el encabezado de la sección en la terminal
    print("\n--- FORMULARIO DE REGISTRO ---")

    # Leemos el estado inicial del JSON
    mock = download(path_file)
    # Mostramos cuántos registros existen antes de añadir el nuevo
    print(f"📊 Estado antes del registro: Hay {len(mock)} registros guardados.")

    # Obtenemos la fecha de hoy en formato AAAA-MM-DD
    date_app = date.today().strftime("%Y-%m-%d")
    print(f"📅 Captura de datos para la fecha: {date_app}")

    # Mostramos el menú de estaciones de Madrid y obtenemos la elegida
    zone = get_valid_zone()

    # Variable para recordar si estamos actualizando o creando uno nuevo
    is_update = False

    # Verificamos si ya existe un registro para esa misma fecha y estación
    if is_duplicate(mock, date_app, zone):
        # Preguntamos en la misma línea y limpiamos espacios con .strip()
        answer = input(f"⚠️ Registro ya existente, ¿desea reemplazarlo? (s/n): ").strip().lower()
        if answer == "s":
            # Eliminamos el registro existente
            mock = [reg for reg in mock if not (reg["fecha"] == date_app and reg["zona"] == zone)]
            # Marcamos que estamos actualizando un registro existente
            is_update = True
        # Si no escribe 's', cancelamos y salimos sin guardar nada
        else:
            return False
    else:
        print(f"✅ Estación '{zone}'. Introduce los datos:")

    # Pedimos y validamos cada medición numérica
    temperature = get_valid_temperature()
    humidity = get_valid_humidity()
    wind = get_valid_wind()
    rain = get_valid_rain()
    

    # Mostramos un resumen de los datos introducidos antes de guardarlos
    print(f"\n📋 Informe: {date_app} | {zone} | {temperature}ºC | {humidity}% | {wind} km/h | {rain} mm")

    # Construimos el diccionario con el nuevo registro (manteniendo claves compatibles con el JSON)
    new_register = {
        "fecha": date_app, 
        "zona": zone,
        "temperatura": temperature,
        "humedad": humidity,
        "viento": wind,
        "lluvia": rain
    } 

    # Añadimos el nuevo diccionario al final de la lista en memoria RAM
    mock.append(new_register)
    # Volcamos la lista completa actualizada al archivo JSON
    save_data(mock, path_file)
    
    # Mostramos el mensaje exacto DESPUÉS de guardar en el archivo
    if is_update:
        # Si estábamos actualizando un registro existente.
        print(f"🔄 Registro actualizado con éxito. Total: {len(mock)} registros guardados.")
    else:
        # Si es un registro nuevo.
        print(f"✅ ¡Nuevo registro guardado! Total: {len(mock)} registros guardados.")

    input("\nPulsa Enter para volver al menú...")   
    return True


def search():
    print("\n--- CONSULTA POR ESTACIÓN / ZONA ---")
    
    # Reutilizamos el selector de estaciones para evitar errores al escribir
    zone = get_valid_zone()
    print(f"\n🔍 Buscando histórico de '{zone}'...")
    
    mock = download(path_file)
    resultados = [reg for reg in mock if reg["zona"].lower() == zone.lower()]
    
    if resultados:
        print(f"📂 Se encontraron {len(resultados)} registros para {zone}:\n")
        for r in resultados:
            print(f"📅 {r['fecha']} | 🌡️ {r['temperatura']}ºC | 💧 {r['humedad']}% | 💨 {r['viento']} km/h | 🌧️ {r['lluvia']} mm")
    else:
        print(f"ℹ️ No hay registros guardados todavía para '{zone}'.")

# Definimos la función que controla el menú principal de la aplicación
def start_app():
    # Este bucle mantiene el programa vivo hasta que el usuario elija Salir
    while True:
        # Imprimimos el marco visual y las opciones del menú
        print("\n==============================")
        print("  APP CLIMÁTICA AYUNTAMIENTO  ")
        print("==============================")
        print("1. Registrar nueva medición")
        print("2. Consultar por zona")
        print("3. Salir")
        
        option = input("\nElige una opción (1-3): ").strip()
        
        # Si elige "1", llamamos a la función de registro
        if option == "1":
            register()
        # Si elige "2", llamamos a la función de consulta por zona
        elif option == "2":
            search()
        # Si elige "3", despedimos al usuario y ejecutamos 'break' para romper el bucle y salir
        elif option == "3":
            print("👋 Cerrando aplicación. ¡Hasta pronto!")
            break
        # Si escribe cualquier otra cosa, mostramos aviso de error y el bucle repite el menú
        else:
            print("❌ Opción no válida. Por favor, escribe 1, 2 o 3.")


# Comprobamos si este archivo se está ejecutando directamente y arrancamos el programa
if __name__ == "__main__":
    # Arrancamos la aplicación llamando al menú principal
    start_app()
