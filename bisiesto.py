# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 17:13:36 2023

@author: BestSystem
"""

def bisiesto(anio):
    return not anio % 4 and (anio % 100 or not anio % 400)

print("los años: ")
for anio in range (2000,2023):
    if bisiesto(anio):
        print(anio, end=' ,')
print("son bisiesto")
