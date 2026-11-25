from store import download

def register():
    print("\n--- FORMULARIO DE REGISTRO ---")

    # 1. Leemos el estado inicial del JSON
    mock = download()
    print(f"📊 Estado antes del registro: Hay {len(mock)} registros guardados.")

    zone = input("Escribe el nombre del parque: ")
    temperature = input("Escribe la temperatureeratura (ºC): ")
    print(f"✅ ¡Genial! Acabas de capturar por consola: {zone} a {temperature}ºC.")

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

