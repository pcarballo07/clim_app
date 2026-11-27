# 📋 Registro de Dailies - App Climática Ayuntamiento

> **Reglas del equipo (máx. 15 min):**
> - Cada persona responde brevemente a las 3 preguntas (*¿Qué hice? ¿Qué haré hoy? ¿Tengo bloqueos?*).
> - **No se resuelven dudas técnicas aquí:** si hay un bloqueo, se anota en el *Parking Lot* y se habla al terminar con las personas implicadas.
> - **Archivos del proyecto:** `main.py`, `validations.py`, `store.py`, `alerts.py`, `data/mock_real.json` y `tests/`.

---

## 🟢 Sprint 0: Preparación y Arranque

### 📅 Día 1 (Sprint 0) - 23/11/2026
* **Scrum Master:** Nayibeth | **Product Owner:** Pablo
* **Resumen de arranque:**
  * **¿Qué hicimos hoy?** Analizar los requisitos del proyecto, definir roles del Sprint 1 y estructurar el tablero Trello con las listas Kanban, etiquetas y tareas de todos los sprints.
  * **¿Qué haremos mañana?** Crear el repositorio en GitHub, configurar los entornos virtuales (`.venv`) y sincronizar Git en los ordenadores de todo el equipo.
  * **¿Bloqueos?** Ninguno.

---

## 🏃‍♂️ Sprint 1: MVP Mínimo (Registro, Validación y Persistencia JSON)

### 📅 Día 2 - 24/11/2026
* **Equipo de desarrollo:**
  * **¿Qué hicimos hoy?** Creamos el repositorio `clim_app` en GitHub con `.gitignore`, `README.md` y `requirements.txt`; configuramos el entorno virtual (`.venv`) y acordamos el *Product Backlog* y la *Definition of Done*.
  * **¿Qué haremos mañana?** Definir la estructura de carpetas (`main.py`, `validations.py`, `store.py`, `alerts.py`, `data/`), los nombres de funciones clave y crear el dataset inicial en `data/`.
  * **¿Bloqueos?** Ninguno.

### 📅 Día 3 - 25/11/2026
* **Subgrupo A (Interfaz y Validaciones):**
  * **¿Qué hicimos hoy?** Creamos el esqueleto del menú en consola (`main.py`) y programamos las validaciones de fechas (`AAAA-MM-DD`) y rangos climáticos en `validations.py` (rama `feat/validaciones`).
  * **¿Qué haremos mañana?** Revisar y hacer *merge* de la PR `feat/validaciones` a `main`, y conectar las validaciones con la captura de inputs (`try/except`) en `main.py`.
  * **¿Bloqueos?** Formato de fecha confirmado (`AAAA-MM-DD`) tras revisar `data/mock_real.json`.

* **Subgrupo B (Datos y Persistencia):**
  * **¿Qué hicimos hoy?** Creamos la estructura de carpetas, generamos los datos históricos reales de Madrid (`data/mock_real.json` y `data/clima_mock.json`) e iniciamos la lectura/guardado del JSON en `store.py`.
  * **¿Qué haremos mañana?** Completar la función de guardado sin pérdida de datos y el control de registros duplicados (misma fecha y zona) en `store.py`.
  * **¿Bloqueos?** Unificar nombres de archivos en la documentación (`store.py` y `validations.py`).

### 📅 Día 4 - 26/11/2026
* **Subgrupo A:**
  * **¿Qué hice?** Fusionamos en `main` las validaciones (`validations.py`) y avanzamos en las funciones de añadir registros y guardar.
  * **¿Qué haré hoy?** Probar el flujo completo de registro desde terminal con datos válidos e inválidos (ej. humedad 110 %, textos en campos numéricos).
  * **¿Bloqueos?** Ninguno.

* **Subgrupo B:**
  * **¿Qué hice?** Ajustamos la lectura y escritura del JSON en `store.py`.
  * **¿Qué haré hoy?** Verificar el control de duplicados por fecha y zona y cerrar las tarjetas pendientes del Sprint 1 en Trello.
  * **¿Bloqueos?** Ninguno.

### 📅 Día 5 - 27/11/2026 *(Plantilla para rellenar)*
* **Subgrupo A:**
  * **¿Qué hice?** 
  * **¿Qué haré hoy?** 
  * **¿Bloqueos?** 

* **Subgrupo B:**
  * **¿Qué hice?** 
  * **¿Qué haré hoy?** 
  * **¿Bloqueos?** 

### 📅 Día 6 (Cierre Sprint 1: Review y Retrospectiva) - 28/11/2026 *(Plantilla para rellenar)*
* **Equipo completo:**
  * **¿Qué hicimos?** Demo corta del MVP mínimo (registro validado y guardado en JSON) y cierre del tablero del Sprint 1.
  * **¿Acuerdos de Retrospectiva?** *(Anotar en `retrospectivas.md`)*.

---

## 🏃‍♀️ Sprint 2: Consultas, Alertas y Calidad (Días 7 - 13)

### 📅 Día 7 - 30/11/2026 *(Plantilla para rellenar)*
* **Subgrupo A (Alertas y Logs - `alerts.py`):**
  * **¿Qué hice?** 
  * **¿Qué haré hoy?** 
  * **¿Bloqueos?** 

* **Subgrupo B (Consultas por zona, Tests y Docs - `tests/` y `README.md`):**
  * **¿Qué hice?** 
  * **¿Qué haré hoy?** 
  * **¿Bloqueos?** 

---
*(Copiar el bloque diario para los días 8 al 12. Recordatorio: el Día 13 se reserva exclusivamente para ensayar y realizar la presentación oral, sin programar).*

