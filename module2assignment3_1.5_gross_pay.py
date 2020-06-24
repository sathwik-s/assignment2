# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:33:13 2020

@author: SATHWIK
"""


r=float(input('enter rate'))
h=float(input('enter hours'))
if h>=40:
    p=1.5*r*h
    print('the pay is',p)
else:
    p=r*h
    print('the pay is',p)