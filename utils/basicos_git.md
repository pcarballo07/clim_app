# Comandos Básicos de Git y GitHub

Guía rápida de referencia con los comandos esenciales de Git y GitHub organizados según el flujo de trabajo habitual.

## 1. Configuración e inicio

* `git init`: Crea un nuevo repositorio local en la carpeta actual.
* `git clone <url>`: Descarga una copia de un repositorio existente desde GitHub a tu equipo.
* `git config --global user.name "<nombre>"`: Configura tu nombre de usuario de forma global.
* `git config --global user.email "<correo>"`: Configura tu correo electrónico de forma global.
* `git config --list`: Muestra la configuración actual de Git.

## 2. Guardar cambios en local

* `git status`: Muestra el estado de los archivos (modificados, nuevos o listos para guardar).
* `git add <archivo>`: Añade un archivo específico al área de preparación (*staging*).
* `git add .`: Añade todos los archivos modificados al área de preparación.
* `git commit -m "<mensaje>"`: Guarda los cambios preparados en el historial con una descripción.

## 3. Sincronizar con GitHub (Remoto)

* `git remote add origin <url>`: Vincula tu repositorio local con uno remoto en GitHub.
* `git push -u origin main`: Sube tus *commits* locales a la rama principal de GitHub por primera vez.
* `git push`: Sube tus nuevos *commits* a GitHub (una vez ya vinculada la rama).
* `git pull`: Descarga y fusiona los cambios más recientes desde GitHub a tu equipo.

## 4. Ramas e historial

* `git branch`: Lista las ramas locales existentes.
* `git checkout -b <nombre-rama>`: Crea una rama nueva y cambia a ella.
* `git checkout <nombre-rama>` (o `git switch <nombre-rama>`): Cambia a una rama existente.
* `git merge <nombre-rama>`: Fusiona los cambios de otra rama en tu rama actual.
* `git log --oneline`: Muestra un resumen compacto del historial de *commits*.
