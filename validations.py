from datetime import datetime


def validate_date(date_str: str) -> bool:
    """Valida que la fecha tenga formato AAAA-MM-DD y sea una fecha real."""
    try:
        datetime.strptime(date_str.strip(), "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_non_empty_text(text: str) -> bool:
    """Valida que un campo de texto (como la zona) no esté vacío."""
    return isinstance(text, str) and len(text.strip()) > 0


def validate_temperature(temp: float) -> bool:
    """Valida que la temperatura esté en un rango lógico (-20°C a 50°C)."""
    return -20.0 <= temp <= 50.0


def validate_humidity(humidity: float) -> bool:
    """Valida que la humedad esté entre 0% y 100%."""
    return 0.0 <= humidity <= 100.0


def validate_wind(wind: float) -> bool:
    """Valida que la velocidad del viento esté entre 0 y 150 km/h."""
    return 0.0 <= wind <= 150.0


def validate_rain(rain: float) -> bool:
    """Valida que la lluvia en mm no sea negativa (0 a 500 mm)."""
    return 0.0 <= rain <= 500.0


def validate_all_ranges(temp: float, humidity: float, wind: float, rain: float) -> tuple[bool, str]:
    """
    Valida todos los valores numéricos de un registro.
    Devuelve (True, 'OK') si todo es válido, o (False, 'Mensaje de error') si algo falla.
    """
    if not validate_temperature(temp):
        return False, "Error: La temperatura debe estar entre -20°C y 50°C."
    if not validate_humidity(humidity):
        return False, "Error: La humedad debe estar entre 0% y 100%."
    if not validate_wind(wind):
        return False, "Error: El viento debe estar entre 0 y 150 km/h."
    if not validate_rain(rain):
        return False, "Error: La lluvia debe ser mayor o igual a 0 mm."
    return True, "OK"

def is_duplicate(data: list, date_app: str, zone: str) -> bool:
    """Comprueba si ya existe un registro para esa misma fecha y zona."""
    for register in data:
        if register["fecha"] == date_app and register["zona"].lower() == zone.lower():
            return True
    return False

