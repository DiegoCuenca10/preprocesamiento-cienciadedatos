import cProfile       # Se importa cProfile
import numpy as np    # Se importa numpy

def es_primo_np(n):        # Funcion para verificar si un numero es primo 
    if n < 2:              # Menor que 2 no es primo 
        return False
    limite = int(np.sqrt(n))
    for i in range(2, limite + 1):        # Verifica los divisores hasta la raiz cuadrada
        if n % i == 0:                    # Si es divisible entonces no es primo 
            return False
    return True

def obtener_primos_np():
    numeros = np.arange(1, 100000)      # Genera el array de numeros usando el numpy
    return [n for n in numeros if es_primo_np(n)]   # Lista de primos usando comprension de las listas 

# Guardar profiling en archivo
cProfile.run("obtener_primos_np()", filename="profiling_optimizado.txt")  # Ejecuta el profiling y se lo guarda en el archivo 

print("profiling_optimizado.txt generado correctamente.")


