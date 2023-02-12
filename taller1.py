# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 13:21:59 2023

@author: personal
"""

#Taller 1 mode 5

"""
1) ¿Cómo obtener período completo en un método de generación de números
aleatorios congruencial lineal?

El período completo en un método de generación de números aleatorios congruencial lineal se refiere
 a la cantidad máxima de números aleatorios distintos que puede producir antes de repetirse.
 Para obtener un período completo, deben cumplirse algunos criterios importantes:

El módulo "M" debe ser un número primo.

La semilla "X0" debe ser un número relativamente primo con respecto a M.

El valor de "a" debe ser un número impar relativamente primo con respecto a M.

El valor de "b" es cualquier número, pero en general se toma un número primo.

Para asegurar que tenemos 
casi el período completo en el importante caso especial definido por c = 0. En la práctica, suele ser conveniente elegir que
m sea una potencia de 2 en una máquina binaria, o una potencia de 10 en una máquina decimal.
Así evitamos la división implícita en la congruencia y la división para formar xi/m.
también la división para formar xi/m. 
2)Use el método congruencial para generar una secuencia de números
aleatorios (entre 0 y 1) considerando:
• X0= 15, a=38, b= 36, M=1000. NO, B no es impar
• X0= 35, a=13, b= 65, M=100. No, X0 no es relativamente primo respecto a M
"""

def congruential_method(X0, a, b, M, n):
    X = [0] * n
    X[0] = X0
    for i in range(1, n):
        X[i] = (a * X[i-1] + b) % M
    return X

X = congruential_method(15, 38, 36, 1000, 5)
print(X)

X = congruential_method(35, 13, 65, 100, 5)
print(X)
