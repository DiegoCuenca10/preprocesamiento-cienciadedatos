
import time
import math

inicio = time.time()

def es_primo(n):
    if n < 2:
        return False
    limite = int(math.sqrt(n)) + 1
    for i in range(2, limite):
        if n % i == 0:
            return False
    return True

primos = [num for num in range(1, 100001) if es_primo(num)]

fin = time.time()

print("La cantidad de numeros primos que se han encontrados:", len(primos))
print("El tiempo de ejecución ya optimizado:", fin - inicio, "segundos")
