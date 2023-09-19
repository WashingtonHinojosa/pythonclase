# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 20:58:03 2023

@author: BestSystem
"""

def readint(prompt, min, max):
    try:
        x = int(input(prompt))
        assert x >= min and x <= max
        return x
    except ValueError:
        print("Error: entrada incorrecta")
        return readint(prompt, min, max)
    except AssertionError:
        print("Error: No esta dentro del rango permitido", min,",", max)
        return readint(prompt, min, max)


v = readint("Enter a number from valor inicil a un valor final: ", -5, 2)

print("The number is:", v)

