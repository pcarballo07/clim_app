# clim_app
Proyecto para desarrollar app que capta información del clima en la comunidad de Madrid y genera una base de datos


## 📊 Origen y Generación de los Datos Históricos (`clima_mock.json`)

Para dotar a la aplicación de un histórico realista que permita consultar tendencias y validar el sistema de alertas desde el primer arranque, el archivo base `data/clima_mock.json` se ha construido a partir de **registros meteorológicos reales de un año completo** de distintas estaciones de la **Comunidad de Madrid** (Madrid Centro, Barajas, Getafe, Alcalá de Henares, Aranjuez, Colmenar Viejo y Puerto de Navacerrada).

### Proceso de extracción y transformación (ETL)
1. **Fuente oficial:** Los datos se han extraído mediante la API pública de **AEMET OpenData** (valores climatológicos diarios).
2. **Normalización de unidades y formatos:** Mediante el script auxiliar de generación (`descargar_aemet.py`), los datos crudos de las estaciones se han limpiado y adaptado al esquema estándar del Ayuntamiento:
   * Conversión de cadenas numéricas con coma decimal (`"18,5"`) a valores numéricos (`float`/`int`).
   * Transformación de la velocidad del viento de $\text{m/s}$ (unidad nativa de AEMET) a $\text{km/h}$.
   * Estandarización de precipitaciones inapreciables (`"Ip"`) a `0.0 mm`.
   * Filtrado de registros incompletos y garantía de unicidad por combinación `fecha` + `zona`.

### Estructura del dataset
Cada entrada del fichero `data/clima_mock.json` sigue el siguiente formato JSON:

```json
{
  "fecha": "2025-07-24",
  "zona": "Madrid Centro",
  "temperatura": 40.8,
  "humedad": 19,
  "viento": 11.4,
  "lluvia": 0.0
}


