# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 00:14:39 2023

@author: BestSystem
"""

nativeVLAN = 1
dataVLAN = 100
if nativeVLAN == dataVLAN:
    print("The native VLAN and the data VLAN are the same.")
else:
    print("This native VLAN and the data VLAN are different.")