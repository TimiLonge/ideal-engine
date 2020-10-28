# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 23:10:40 2019

@author: timil
"""

my_string = "StopAndSmellTheRoses"
i = 0
result = ""
for c in my_string:
    if c.isupper() and i > 0:
        result += " "
        result += c.lower()
    else:
        result += c
    i += 1

print (result)