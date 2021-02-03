#!/usr/bin/env python3
"""
EJERCICIO 1: Implemente en lenguaje Python una función que aproxime mediante
un Polinomio de Taylor de tercer orden centrado en x=1 para predecir f(2),
siendo f(x) = 25x**3 – 6x**2 + 7x – 88. Calcule luego el error relativo de la
aproximación.

EJERCICIO 2: Implemente en lenguaje Python el método de Newton-Raphson para
aproximar la solución de f(x) = 0, siendo f(x) = exp(-x)-ln(x).

Escriba aqui los nombres de los integrantes del grupo:

- Luisana Hernández.
"""
import math

# AQUÍ ABAJO EL CÓDIGO DE LUISANA.



# AQUÍ ABAJO EL CÓDIGO DE EDGARD.

def derivada(funcion, h=0.01):
    """Calcula la derivada de una función.

    Parámetros:
    -----------
    funcion: es una función de una variable.
    h: es un número real fijo.

    Retorna:
    --------
    Retorna una función que es la derivada del parámetro función.
    """
    def df(x):
        return (funcion(x+h) - funcion(x))/h
    return df


def newton_raphson(funcion, x0, er, N, dec=4):
    """Implementa y Ejecuta el Método de Newton-Raphson.

    Parámetros:
    -----------
    funcion: es la función a resolver f(x) = 0
    x0: es un número real y aproximación inicial.
    er: es la cota del error, criterio de parada.
    N: número máximo de iteraciones.
    dec: número de decimales.
    """
    error = 1 # Error inicial.
    itera = 0 # Número de interación.
    derf  = derivada(funcion)

    print("Iteraciones:")
    print("------------")
    while (error > er) and (itera < N):
        itera += 1
        xn = x0 - (funcion(x0)/derf(x0))
        error = math.fabs((xn - x0)/xn)
        print("i =", itera, "x0 =", x0, "xn =", xn, "Error =", error)
        x0 = xn

    print("\nComprobación:")
    print("-------------")
    print("f({}) = {}".format(xn, funcion(xn)))


if __name__ == "__main__":
    # Testing ...

    funcion = lambda x: math.exp(-x) - math.log(x)
    x0 = 2
    er = 0.01
    N  = 100

    newton_raphson(funcion, x0, er, N)