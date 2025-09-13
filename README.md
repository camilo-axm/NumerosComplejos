# Librería de Números Complejos en Python

En este proyecto se pueden implementar operaciones entre números complejos sin usar el tipo `complex` de Python.  
Los números complejos se modelan como tuplas `(real, imaginario)` y en coordenadas polares como `(módulo, ángulo)`.

## Funcionalidades
La librería puede realizar las siguientes operaciones:
- Suma
- Resta
- Producto
- División
- Módulo
- Conjugado
- Conversión entre forma cartesiana ↔ polar
- Obtener la fase de un número complejo
  
Operaciones básicas con números complejos
Se realizan sumas, productos y divisiones de números complejos, además de calcular su conjugado y módulo, verificando los resultados manualmente y con Python.

Visualización en el plano complejo
Se implementa una función para graficar números complejos y sus conjugados. Luego se extiende para mostrar gráficamente la suma y la multiplicación de dos números complejos en el plano.

Conjunto de Mandelbrot
Se modifica el código del conjunto de Mandelbrot para aplicar zoom en diferentes centros y variar el número máximo de iteraciones (max_iter), observando cómo cambian el detalle y el tiempo de cómputo del fractal.

Conjunto de Julia
Se implementa un generador del conjunto de Julia usando iteraciones de la forma z = z*z + constante. Se exploran distintos valores de la constante para analizar cómo cambia la forma del fractal.

Propiedades de los números complejos
Se demuestran y verifican en Python dos propiedades fundamentales:

El valor absoluto de un producto es igual al producto de los valores absolutos.

El conjugado de una suma es la suma de los conjugados.
    
