# -*- coding: utf-8 -*-
"""Punto_3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZiyRAcj_CGbNygrrPEzEs78R9cSKuUbP
"""

def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def primos_en_lista(lista):
    primos = []
    for numero in lista:
        if es_primo(numero):
            primos.append(numero)
    return primos

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primos = primos_en_lista(numeros)
print("Los números primos en la lista son:", primos)