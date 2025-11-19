## 1. Introducción
El objetivo del codigo original realizado fue encontrar todos los numeros que sean primos dentro de un rango de 1 a 100,000 en donde encontramos algunos problemas entre ellos el principal 
el cual fue que el del bajo rendimiento esto se debe a que se utilizo un bucle el cual probaba cada uno de los divisores desde 1 hasta n, como tambien no aplique metodos matematicos mas 
eficientes como puede ser el uso de la raiz cuadrada y tambien no existio ningun tipo de analisis de rendimiento por lo tanto esto dio como resultado a un tiempo de ejcucion muy alto y de un
uso innecesario de CPU.
##  Optimización:
Para mejorar el rendimiento del codigo original se aplicaron varias tecnicas las cuales fueron 

- ## Uso de la raiz cuadrada
En el cual se modifico el algoritmo que es el encargado de verificar si el numero es primo que tiene como objetivo pobrar divisores hasta raiz cuadrada de n esto tiene como objetivo acelerar su 
proceso mediante reduccion de cantidades de operaciones.

- ## List Comprehensions
En el cual se uso con la finalidad de reemplazar los bucles que se utilizan tradicionalmente por una list comprehensions en este caso se utilizo: 
[n for n in range(1, 100000) if es_primo(n)]

- ## Uso de Numpy
En cual se la utilizo en la version mas optimizada con la finalidad de generar rangos de numeros que sean mas eficientes, calcular las raices cuadradas de manera eficiente como por ejemplo:
numeros = np.arange(1, 100000)
Estas mejoras tienen como objetivo mejorar reducir el tiempo total adicional de la ejecucion para que sea mas rapida que la original

## Resultados:
Los resultados obtenidos mediante el codigo original y el codigo optimizado reflejan una comparativa de tiempos en donde los tiempos obtenidos se guardaron en el archivo tiempos.txt.
Los resultados obtenidos fueron los siguientes:

- ## Codigo original:
Tiempo obtenido: 0.3914 segundos

- ## Codigo optimizado (Numpy) :
Tiempo obtenido: 1.0073 segundos

Podemos observar que el tiempo de ejecucion del codigo obtimizado utilizando el cProfile es mayor debido a que este añade mas cargas extras lo cual hace que la ejecucion sea mas lenta.
Por lo tanto sin el uso de cProfile la version optimizada seria mas eficiente debido a que habran menos iteraciones por el uso de la raiz cuadrada, mejor manejo de las listas y el uso de NUmpy

## Analisis de cProfile 
En el analisis de cProfile en el "archivo profiling_original.txt" nos ayuda a mostrar que:

-Que la funcion que se utiliza en la cual mas tiempo consume es [ es_primo() ]

- La creacion de la lista de los primos tambien tiene un consumo importante en [ (obtener_primos() ]

En el analisis de cProfile en el archivo " profiling_optimizado.txt " nos ayuda a mostrar que:

- Que la funcion que mas tiempo consume es [ es_primo_np() ]

- Se utilizo Numpy la cual se implemento funciones adicionales que tambien consumen mas tiempo

- Como asi mismo las llamadas repetitivas hacen que la version de Numpy se mas lenta que la original

  ## Conclusiones
  En conclusion, el codigo optimizado permitio el analisis del rendimiento del codigo mediante la aplicacion de tecnicas como la raiz cuadrada, list comprehensions y NumPy pero el tiempo
  del codigo optimizado fue un poco mayor debido a esto el proceso realizado nos ayudado en entender como afectan estas herramientas al desempeño del codigo. Algunas recomendaciones para futuro
  puede ser la utilizacion de algoritmos mas eficientes, evitar el Numpy en muchos bucles pequeños debido a que no siempre acelera su proceso.

  ## Anexos

- ## profiling_original
<img width="1019" height="649" alt="image" src="https://github.com/user-attachments/assets/d05bb193-99e9-4f2f-af3f-ff84535cbe44" />

- ## profiling_optimizado
<img width="1017" height="618" alt="image" src="https://github.com/user-attachments/assets/6df4c856-dea5-409c-a4d8-fd08c3930ebb" />

- ## tiempos
<img width="1008" height="531" alt="image" src="https://github.com/user-attachments/assets/fb0cfb2f-b38c-4716-ae2e-346a2d3dda1c" />
<img width="1013" height="622" alt="image" src="https://github.com/user-attachments/assets/f1bf8fdf-675c-4fc2-8639-e486125d8ce2" />
<img width="1017" height="697" alt="image" src="https://github.com/user-attachments/assets/8dff9b7f-059b-4969-8780-87dbde7837cb" />

- ## Graficos
<img width="1018" height="549" alt="image" src="https://github.com/user-attachments/assets/7ccc3246-a5f6-49a4-92c9-ad043b251433" />

- ## comparativa_tiempos.png
<img width="1020" height="645" alt="image" src="https://github.com/user-attachments/assets/58879662-ab1c-4dca-8ffe-b2b5a4bd3791" />

- ## distribucion_tiempos.png
<img width="1014" height="644" alt="image" src="https://github.com/user-attachments/assets/682dddd7-ab6f-43cc-90f9-8833fe06d850" />









