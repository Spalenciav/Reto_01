

# Reto-uno

# Punto 1
**Problema:** Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).
# Solución:
Se comienza definiendo la función "operacion_basica" que recibe 3 argumentos: dos números y un operador. Luego, dependiendo del operador que corresponda, se realiza la operación. El código continúa con la entrada de los números y el operador. Finalmente, se imprime el resultado.

# Punto 2
**Problema:** Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.
# Solución:
El código comienza con la función "es_palindromo", diseñada para verificar si una palabra es un palíndromo, tomando la palabra como argumento. Luego, se inicia convirtiendo todas las letras de la palabra a minúsculas para evitar problemas de sensibilidad a mayúsculas y minúsculas durante la comparación. Posteriormente, se calcula la longitud de la palabra y se guarda en la variable "longitud". Después, el bucle for itera sobre la mitad de la longitud de la palabra, ya que para verificar si una palabra es un palíndromo solo necesitamos comparar la primera mitad con la segunda mitad (en orden inverso). Este enfoque mejora la eficiencia del algoritmo.

# Punto 3
**Problema:** Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.
# Solución:
Este código consiste en dos funciones: "es_primo" y "primos_en_lista". La función "es_primo" verifica si un número es primo, tomando el número como argumento. Inicia comprobando si el número es menor o igual a 1, en cuyo caso devuelve Falso. Luego, para números menores o iguales a 3, devuelve Verdadero ya que son primos. Si el número es divisible por 2 o 3, devuelve Falso. Después, se utiliza un bucle while para iterar desde 5 hasta la raíz cuadrada del número. Durante cada iteración, se verifica si el número es divisible por i o i + 2. Si lo es, devuelve Falso, indicando que el número no es primo. Si pasa todas estas comprobaciones, devuelve Verdadero. La función "primos_en_lista" toma una lista de números y devuelve una lista que contiene solo los números primos de la lista original, utilizando la función "es_primo". Se proporciona un ejemplo de uso, donde se crea una lista de números del 1 al 10 y se llama a "primos_en_lista" con esa lista como argumento. Luego, se imprime la lista resultante de números primos.

# Punto 4
**Problema:** Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
# Solución:
Este código se define en una función llamada "mayor_suma_consecutiva" que calcula la mayor suma entre dos elementos consecutivos en una lista dada. Primero, se verifica si la lista tiene menos de dos elementos; en ese caso, no es posible realizar una suma consecutiva, por lo que devuelve None. Después, inicializa la variable "mayor_suma" con la suma de los dos primeros elementos de la lista. Luego, itera sobre la lista y calcula la suma de cada par de elementos consecutivos. Si encuentra una suma mayor que la "mayor_suma" actual, actualiza el valor de "mayor_suma". Finalmente, devuelve la "mayor_suma" encontrada. Se proporciona un ejemplo de uso donde se aplica la función a una lista de números del 1 al 10, mostrando la mayor suma consecutiva entre dos elementos.

# Punto 5
**Problema:** Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]
# Solución:
El código define una función llamada "mismos_caracteres" que toma una lista de palabras como entrada y devuelve una nueva lista que contiene solo aquellas palabras que tienen todos los caracteres únicos, es decir, donde cada letra en la palabra es única. En el bucle "for", itera sobre cada palabra en la lista de entrada y utiliza la función "set" para convertir la palabra en un conjunto de caracteres únicos. Luego, compara la longitud del conjunto de caracteres únicos con la longitud original de la palabra. Si son iguales, significa que todos los caracteres en la palabra son únicos, por lo que se agrega la palabra a la lista "resultado". Finalmente, se proporciona un ejemplo de uso donde se aplica la función a una lista de palabras y se muestra la lista resultante de palabras con caracteres únicos.

