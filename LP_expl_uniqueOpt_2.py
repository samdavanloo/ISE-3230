#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:39:46 2019

@author: Sam
"""

from cvxopt.modeling import variable,op
x_1 = variable()
x_2 = variable()
c1 = ( 2*x_1+x_2 <= 100 )
c2 = ( x_1+x_2 <= 80 )
c3 = ( x_1 <= 40 )
c4 = ( x_1>=0 )
c5 = ( x_2>=0 )
lp1 = op(-3*x_1-2*x_2, [c1,c2,c3,c4,c5])
lp1.solve()
lp1.status
print(x_1.value)
print(x_2.value)
print(lp1.objective.value())
