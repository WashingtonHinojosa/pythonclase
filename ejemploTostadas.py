# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:31:54 2023

@author: BestSystem
"""

from ejemplo.paquetes.tostadas_pipo.utilidades import calculos
from ejemplo.paquetes.tostadas_pipo.utilidades import impuestos

monto = int(input("Introduzca un monto entero: "))
monto_suma = int(input("Introduzca un monto entero a sumar: "))

suma= calculos.suma_total(monto_suma)+impuestos.impuesto_iva14(monto)

print ("Total a Facturar: {0} BsS, con IVA 14%.".format(suma) )


