#  Informe y Documentación

## Introducción
Este proyecto desarrollado tiene como objetivo estudiar y aplicar el Git ademas del GitHub para poder controlar versiones y automatizar los flujos de trabajo que se desarrollaran dentro del entorno

La funcionalidad implementada fue el desarrollo de un script en Python llamada preprocesamiento.py en donde encontramos las funciones esenciales como: limpieza de datos, normalizacion de los datos (datasets) y la preparacion de la informacion para su analisis.

## Comandos Git usados
Los comando de Git usados son:

Git clone : Ayuda a clonar el repositorio desde el GitHub

Git checkout -b feature-preprocesamiento: Ayuda a crear una nueva rama

Git add: Agregar los archivos en la área de preparación

Git commit -m: Ayuda a guardar los cambios de manera local

Git push origin rama: Sube los cambios que se realizan al repositorio remoto

Git merge: Ayuda a fusionar las ramas

## Automatización (GitHub Actions)
Se realizo un flujo de trabajo a travez de GitHub Actions en donde se ejecuta el script de Python en el repositorio 

name: Flujo trabajo Python
on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Instalar dependencias
        run: pip install pandas
      - name: Ejecutar script
        run: python preprocesamiento.py
  ## EVIDENCIAS
  
  ## ▪ Comandos ejecutados
  
<img width="843" height="467" alt="image" src="https://github.com/user-attachments/assets/6083a643-9c15-4371-a2d3-3c0669eed35a" />
<img width="940" height="471" alt="image" src="https://github.com/user-attachments/assets/cc55a399-5137-4e10-aa83-285a26ca317f" />
<img width="901" height="473" alt="image" src="https://github.com/user-attachments/assets/2830c8c5-d1a6-4391-90b1-3355bcd90748" />

 ## ▪ Pull request y fusión en GitHub.
 
 <img width="767" height="406" alt="image" src="https://github.com/user-attachments/assets/0ed29172-0fcb-416e-a464-a7ff06b84e8c" />
 <img width="801" height="426" alt="image" src="https://github.com/user-attachments/assets/9fb4d173-8703-4aac-831b-13c6a8eb7135" />
 
 ## ▪ Ejecución exitosa de GitHub Actions.
 
 <img width="861" height="484" alt="image" src="https://github.com/user-attachments/assets/f5146e92-4b11-4ba9-9832-0de8e3f28f59" />
 <img width="877" height="493" alt="image" src="https://github.com/user-attachments/assets/d15fd597-c720-4500-9d90-37f2c0f3e801" />








