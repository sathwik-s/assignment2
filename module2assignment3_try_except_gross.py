# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:34:51 2020

@author: SATHWIK
"""


h=float(input('enter hours'))
try:
    r=input('enter rate')
    int(r)
    pay=h*r
    print('pay is',pay)
except:
    print('invalid input')