def evaluate_alerts(record: dict) -> list[str]:
    """
    Evalúa un registro climático y devuelve una lista con las alertas activadas.
    Claves esperadas en 'record': 'temperatura', 'viento', 'lluvia'.
    """
    alerts = []

    temp = record.get("temperatura", 0.0)
    wind = record.get("viento", 0.0)
    rain = record.get("lluvia", 0.0)

    # 1. Alerta por calor extremo
    if temp >= 40.0:
        alerts.append("🔴 ALERTA ROJA POR CALOR EXTREMO (>= 40°C)")
    elif temp >= 35.0:
        alerts.append("🟠 ALERTA NARANJA POR CALOR (>= 35°C)")

    # 2. Alerta por viento fuerte
    if wind >= 70.0:
        alerts.append("💨 ALERTA POR VIENTO FUERTE (>= 70 km/h)")

    # 3. Alerta por lluvia intensa
    if rain >= 30.0:
        alerts.append("🌧️ ALERTA POR LLUVIA INTENSA (>= 30 mm)")

    return alerts
