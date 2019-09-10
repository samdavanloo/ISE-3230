#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:31:42 2019

@author: Sam
"""

from cvxopt.modeling import variable,op
x_1 = variable()
x_2 = variable()
c1 = ( (2/3)*x_1+x_2 <= 18 )
c2 = ( 2*x_1+x_2 >= 8 )
c3 = ( x_1 <= 12 )
c4 = ( x_2 <= 16 )
c5 = ( x_1>=0 )
c6 = ( x_2>=0 )
lp1 = op(-x_1-x_2, [c1,c2,c3,c4,c5,c6])
lp1.solve()
lp1.status
print(x_1.value)
print(x_2.value)
print(lp1.objective.value())
