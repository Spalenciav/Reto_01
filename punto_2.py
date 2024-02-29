# -*- coding: utf-8 -*-
"""Punto_2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cX4C9rt7q616HQE21tyMCvA98Bmd1xpd
"""

def es_palindromo(palabra):
    palabra = palabra.lower()
    longitud = len(palabra)
    for i in range(longitud // 2):
        if palabra[i] != palabra[longitud - i - 1]:
            return False
    return True

palabra = input("Ingrese una palabra para verificar si es un palíndromo: ")
if es_palindromo(palabra):
    print("La palabra '{}' es un palíndromo.".format(palabra))
else:
    print("La palabra '{}' no es un palíndromo.".format(palabra))