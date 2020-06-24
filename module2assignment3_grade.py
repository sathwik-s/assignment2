# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:34:03 2020

@author: SATHWIK
"""


  
s=float(input('enter the score in between 0 and 1 '))
if s>0 and s<1:
    if s>=0.9:
        print('grade is A')
    elif s>=0.8:
        print('grade is B')
    elif s>=0.7:
        print('grade is C')
    elif s>=0.6:
        print('grade id D')
    else:
        print('grade is F')
else:
    print('invalid input')