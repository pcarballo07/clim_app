from datetime import datetime


# Constante de tipo diccionario que relaciona el nombre de cada estación con su código oficial AEMET
MADRID_STATIONS = {
    "Madrid Centro": "3195",        # Estación de Madrid, Parque del Retiro
    "Madrid Barajas": "3129",       # Estación de Madrid, Aeropuerto
    "Getafe": "3200",               # Estación de Getafe
    "Alcalá de Henares": "3170Y",   # Estación de Alcalá de Henares
    "Aranjuez": "3100B",            # Estación de Aranjuez
    "Colmenar Viejo": "3191E",      # Estación de Colmenar Viejo
    "Navacerrada": "2462",          # Estación del Puerto de Navacerrada
}


# Definimos una función que recibe una lista de registros, una fecha y una zona, y devuelve True o False
def is_duplicate(data: list, date: str, zone: str) -> bool:
    """Comprueba si ya existe un registro guardado para esa misma fecha y zona."""
    # Recorremos uno por uno cada diccionario (registro) dentro de la lista histórica
    for record in data:
        # Comprobamos si coincide la fecha exacta Y el nombre de la zona (pasando ambos a minúsculas)
        if record["fecha"] == date and record["zona"].lower() == zone.lower():
            # Si encontramos coincidencia, devolvemos True inmediatamente (sí está duplicado)
            return True
    # Si termina todo el bucle sin encontrar coincidencias, devolvemos False (no está duplicado)
    return False


# Definimos una función sin parámetros que devolverá un texto (str) con la zona válida
def get_valid_zone() -> str:
    """Muestra las estaciones de Madrid disponibles y devuelve el nombre oficial elegido."""
    # Extraemos solo las claves (nombres) del diccionario y las convertimos en una lista ordenada
    zone_names = list(MADRID_STATIONS.keys())
    
    # Imprimimos un encabezado visual en la consola
    print("\n--- ELIGA UNA DE LAS SIGUIENTES ZONAS ---")
    # Recorremos la lista obteniendo a la vez un número de índice empezando en 1 y el nombre de la estación
    for index, name in enumerate(zone_names, start=1):
        # Buscamos el código AEMET correspondiente a ese nombre dentro del diccionario
        station_code = MADRID_STATIONS[name]
        # Mostramos por pantalla la opción numerada (ej. "1. Madrid Centro (AEMET Station: 3195)")
        print(f"{index}. {name} (AEMET Station: {station_code})")
        
    # Iniciamos un bucle infinito que se repetirá hasta que el usuario elija una opción válida
    while True:
        # Abrimos un bloque seguro para atrapar errores si el usuario no escribe un número entero
        try:
            # Pedimos el dato, quitamos espacios sobrantes (.strip()) y lo convertimos a entero (int)
            choice = int(input(f"\nSelect station number (1-{len(zone_names)}): ").strip())
            
            # Comprobamos si el número elegido está entre 1 y el total de estaciones disponibles (7)
            if 1 <= choice <= len(zone_names):
                # Restamos 1 porque las listas en Python empiezan en 0, y devolvemos el nombre elegido
                return zone_names[choice - 1]
            
            # Si el número estaba fuera de rango (ej. 0 o 9), avisamos y el bucle vuelve a empezar
            print(f"❌ Error: Please choose a number between 1 and {len(zone_names)}.")
        # Si la conversión int() falló porque escribió letras o dejó vacío, capturamos el ValueError
        except ValueError:
            # Mostramos un mensaje claro sin que el programa se cierre y volvemos a pedir el dato
            print("❌ Error: You must enter a valid option number (e.g., 1).")


# Definimos la función que pedirá y validará la temperatura devolviendo un número decimal (float)
def get_valid_temperature() -> float:
    """Pide la temperatura por consola y valida que esté en un rango lógico (-20°C a 50°C)."""
    # Bucle infinito hasta lograr una temperatura válida
    while True:
        # Bloque seguro contra entradas que no sean números
        try:
            # Leemos texto, quitamos espacios, cambiamos comas por puntos y convertimos a decimal (float)
            temp = float(input("Enter temperature (°C): ").strip().replace(",", "."))
            # Verificamos que la temperatura esté dentro de los límites lógicos permitidos
            if -20.0 <= temp <= 50.0:
                # Si es válida, salimos de la función entregando el valor
                return temp
            # Si está fuera de rango (ej. 80°C), mostramos el error y repetimos el bucle
            print("❌ Error: Temperature must be between -20.0°C and 50.0°C.")
        # Si el usuario escribió texto (ej. "calor"), atrapamos el fallo aquí
        except ValueError:
            # Avisamos del error de formato y damos otra oportunidad
            print("❌ Error: Please enter a valid number (e.g., 22.5).")


# Definimos la función que pedirá y validará la humedad devolviendo un decimal (float)
def get_valid_humidity() -> float:
    """Pide la humedad relativa y valida que esté entre 0% y 100%."""
    # Bucle infinito hasta lograr una humedad válida
    while True:
        # Bloque seguro contra texto inválido
        try:
            # Leemos, limpiamos espacios, normalizamos coma a punto y convertimos a float
            humidity = float(input("Enter humidity (%): ").strip().replace(",", "."))
            # Comprobamos que el porcentaje sea físicamente posible (entre 0 y 100)
            if 0.0 <= humidity <= 100.0:
                # Devolvemos la humedad válida y terminamos la función
                return humidity
            # Si puso 110% o -5%, avisamos y volvemos a pedir
            print("❌ Error: Humidity must be between 0% and 100%.")
        # Capturamos el error si no introdujo un número
        except ValueError:
            # Mensaje de error claro para reintentar
            print("❌ Error: Please enter a valid number (e.g., 45).")


# Definimos la función que pedirá y validará la velocidad del viento en km/h
def get_valid_wind() -> float:
    """Pide la velocidad del viento y valida que esté entre 0 y 150 km/h."""
    # Bucle infinito hasta obtener un viento válido
    while True:
        # Bloque seguro contra errores de conversión
        try:
            # Capturamos entrada, limpiamos formato y convertimos a decimal
            wind = float(input("Enter wind speed (km/h): ").strip().replace(",", "."))
            # Validamos que no sea negativo ni supere el límite máximo (150 km/h)
            if 0.0 <= wind <= 150.0:
                # Entregamos el valor válido
                return wind
            # Aviso si el número está fuera de rango
            print("❌ Error: Wind speed must be between 0 and 150 km/h.")
        # Capturamos fallo si escribió letras
        except ValueError:
            # Aviso para que vuelva a intentarlo
            print("❌ Error: Please enter a valid number (e.g., 12.0).")


# Definimos la función que pedirá y validará el volumen de lluvia en milímetros
def get_valid_rain() -> float:
    """Pide el volumen de precipitación y valida que esté entre 0 y 500 mm."""
    # Bucle infinito hasta obtener un dato válido de lluvia
    while True:
        # Bloque seguro contra entradas no numéricas
        try:
            # Leemos entrada, quitamos espacios, cambiamos coma por punto y convertimos a float
            rain = float(input("Enter rainfall volume (mm): ").strip().replace(",", "."))
            # Verificamos que no sea lluvia negativa y esté dentro del tope de 500 mm
            if 0.0 <= rain <= 500.0:
                # Devolvemos el valor validado
                return rain
            # Aviso si el número es negativo o mayor de 500
            print("❌ Error: Rainfall must be between 0 and 500 mm.")
        # Capturamos error si escribió letras o dejó el campo vacío
        except ValueError:
            # Aviso claro para volver a pedir el dato
            print("❌ Error: Please enter a valid number (e.g., 0.0).")


