#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:59:11 2019

@author: Sam
"""

from cvxopt.modeling import variable,op
x_1 = variable()
x_2 = variable()
c1 = ( 2*x_1+x_2 <= 16 )
c2 = ( x_1+x_2 <= 10 )
c3 = ( x_1>=0 )
c4 = ( x_2>=0 )
lp1 = op(-6*x_1-3*x_2, [c1,c2,c3,c4])
lp1.solve()
lp1.status
print(x_1.value)
print(x_2.value)
print(lp1.objective.value())
print(c1.multiplier.value)
print(c2.multiplier.value)
print(c3.multiplier.value)
print(c4.multiplier.value)
