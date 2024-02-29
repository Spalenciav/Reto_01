# Reto-uno

# Punto 1
**Problema:** Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).
# Pasos para la solución:
1. **Definición de la función operacion(a):** La función operacion toma una lista a como argumento. Esta función evalúa el tercer elemento de la lista a para determinar el tipo de operación a realizar.
2. **Determinación de la operación:** Se utiliza un condicional if-elif-else para identificar el tipo de operación basado en el tercer elemento de la lista a.
3. **Realización de la operación:** Si el tercer elemento de a es +, -, *, /, se realiza una dicha operación utilizando los primeros dos elementos de la lista a.
4. **Manejo de casos especiales:** Se verifica si el segundo elemento de a es cero en el caso de una división para evitar una división por cero.
5. **Casos no definidos:** En caso de que el usuairo ingrese datos incoherentes se imprime un mensaje de erro. 

# Punto 2
**Problema:** Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.
# Pasos para la solución:
1. **Definición de la función palindromo(a):** La función palindromo toma una cadena de texto a como argumento.
2. **Inicialización de la variable x:** La variable x se inicializa en -1. Esto se utiliza para acceder a los elementos de a en orden inverso.
3. **Bucle for para verificar palíndromos:** Se utiliza un bucle for para iterar sobre cada caracter i en la cadena a. En cada iteración, se verifica si el caracter i es diferente del caracter correspondiente en la posición inversa de a. Si se encuentra algún par de caracteres diferentes, se devuelve "No es palíndromo".
Se decrementa x después de cada iteración para acceder a los caracteres de a en orden inverso.
4. **Resultado de la función:** Si el bucle for completa su ejecución sin encontrar ningún par de caracteres diferentes, se devuelve un mensaje indicando que la cadena es un palíndromo.

# Punto 3
**Problema:** Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.
# Pasos para la solución:
1. **Definición de la función primos(a):** La función primos toma una lista de números a como argumento.
2. **Inicialización de la lista x:** La lista x se inicializa como una lista vacía. Esta lista se utilizará para almacenar los números primos encontrados en la lista de entrada a.
3. **Bucle for para verificar los números primos:** Se utiliza un bucle for para iterar sobre cada número i en la lista a. Se verifica si i es menor que 2. Si es así, se omite este número y se pasa al siguiente mediante continue, ya que los números primos son mayores que 1. Se inicializa la variable primo como verdadera (True). Esta variable se utilizará para determinar si i es primo o no. Se utiliza otro bucle for para iterar sobre los números de 2 hasta la raíz cuadrada de i más 1. En cada iteración, se verifica si i es divisible por j. Si lo es, significa que i no es primo y se establece primo como falso (False).
Si ningún número j entre 2 y la raíz cuadrada de i divide exactamente a i, primo sigue siendo verdadero, lo que significa que i es primo. Si primo es verdadero después de verificar todos los números j, se agrega i a la lista x.
4. **Resultado de la función:** Se devuelve un mensaje que indica los números primos encontrados en la lista a.

# Punto 4
**Problema:** Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
# Pasos para la solución:
1. **Definición de la función suma_mayor(a):** Se define una función llamada suma_mayor que toma una lista de números enteros a como argumento.
2. **Ordenamiento de la lista:** Se ordena la lista a utilizando la función sorted(). Esto garantiza que los números estén en orden ascendente.
3. **Inicialización de la variable x:** Se inicializa la variable x con el valor -1. Esta variable se utilizará para acceder a los elementos de a en orden inverso.
4. **Bucle for para encontrar los elementos consecutivos de mayor valor:** Se utiliza un bucle for para iterar sobre los índices de a desde 0 hasta len(a) - 2.
En cada iteración, se compara la diferencia entre el elemento actual a[x] y el elemento anterior a[x-1].
Si la diferencia es 1 o -1, significa que los elementos son consecutivos. Se devuelve un mensaje que indica los dos elementos de mayor valor consecutivo encontrados y su suma.
5. **Manejo de casos especiales:** Si no se encuentran elementos consecutivos, se devuelve un mensaje indicando que no existen dichos elementos.

# Punto 5
**Problema:** Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]
# Pasos para la solución:
1. **Definición de la función mismos_caracteres(a):** Se define una función llamada mismos_caracteres que toma una lista de palabras a como argumento.
2. **Inicialización de la lista x:** Se inicializa la lista x como una lista vacía. Esta lista se utilizará para almacenar las palabras que tienen los mismos caracteres que al menos una otra palabra en la lista a.
3. **Bucle for anidado para comparar palabras:** Se utiliza un bucle for externo para iterar sobre los índices de la lista a. Dentro del bucle externo, se utiliza otro bucle for para iterar sobre los índices restantes en a. Se crea un conjunto de caracteres (conjunto_palabra) para la palabra actual en el bucle externo. Se crea otro conjunto de caracteres (conjunto_comparar) para la palabra actual en el bucle interno.
Si los conjuntos son iguales y la palabra actual en el bucle interno no está en la lista x, se agrega tanto la palabra del bucle externo como la palabra del bucle interno a la lista x.
4. **Resultado de la función:** Se devuelve un mensaje que indica las palabras que tienen los mismos caracteres con al menos una otra palabra en la lista a. Los conjuntos se utilizan para evitar duplicados en la lista x.

   
