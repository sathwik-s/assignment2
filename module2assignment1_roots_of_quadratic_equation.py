# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:21:01 2020

@author: SATHWIK
"""


import cmath
import math
a=float(input('enter a'))
b=float(input('enter b'))
c=float(input('enter c'))
d=b*b-4*a*c
if d>0:
    r1=(-b+math.sqrt(d))/2*a
    r2=(-b-math.sqrt(d))/2*a
    print('roots are real',r1,r2)
elif d<0:
    r1=(-b+cmath.sqrt(d))/2*a
    r2=(-b+cmath.sqrt(d))/2*a
    print('root are imaginary ',r1,r2)
elif d==0:
    r=-b/2*a
    print('roots are equal',r,r)
else:
    print('invalid input')