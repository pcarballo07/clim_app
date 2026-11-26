from store import download, save_data
from validations import is_duplicate
from datetime import date

path_file = "data/mock_real.json"

def register():
    print("\n--- FORMULARIO DE REGISTRO ---")

    # 1. Leemos el estado inicial del JSON
    mock = download()
    print(f"📊 Estado antes del registro: Hay {len(mock)} registros guardados.")

    date_app = date.today().strftime("%Y-%m-%d")
    print(f"Captura de datos para la fecha: {date_app}")
    zone = input("Escribe el nombre de la zona: ")
    temperature = input("Escribe la temperatura (ºC): ")
    humidity = input("Escribe la humedad (%): ")
    wind = input("Escribe la velocidad del viento (km/h): ")
    rain = input("Escribe el volumen de precipitacion (mm): ")
    print(f"Informe: {date_app} {zone} {temperature} {humidity} {wind} {rain} ")

    if is_duplicate(mock, date_app, zone):
        print(f"Registro duplicado")
        return False
    else:
        print(f"No existe duplicado")
    
    print(type(mock))

    new_register = {
        "fecha": date_app, 
        "zona": zone,
        "temperatura": temperature,
        "humedad": humidity,
        "viento": wind,
        "lluvia": rain
    } 

    mock.append(new_register)
    print(f"📊 Estado después del registro: Hay {len(mock)} registros guardados.")
    
    save_data(mock, path_file)

def search():
    print("\n--- CONSULTA POR zone ---")
    zone = input("¿Qué parque buscas?: ")
    print(f"🔍 Buscando datos de '{zone}' en el archivo JSON...")

def start_app():
    # Este bucle mantiene el programa vivo hasta que el usuario elija Salir
    while True:
        print("\n==============================")
        print("  APP CLIMÁTICA AYUNTAMIENTO  ")
        print("==============================")
        print("1. Registrar nueva medición")
        print("2. Consultar por zone")
        print("3. Salir")
        
        option = input("\nElige una opción (1-3): ")
        
        if option == "1":
            register()
        elif option == "2":
            search()
        elif option == "3":
            print("👋 Cerrando aplicación. ¡Hasta pronto!")
            break  # Rompe el bucle y termina el programa
        else:
            print("❌ Opción no válida. Por favor, escribe 1, 2 o 3.")

# Arrancamos el programa
if __name__ == "__main__":
    start_app()

