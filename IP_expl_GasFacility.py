#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:55:48 2019

@author: Sam
"""

import numpy as np
import cvxpy as cp

x = cp.Variable((3,1), boolean = True) # matrix variable
y = cp.Variable((3,2), nonneg  = True) # matrix variable

constraints = []
constraints.append(y[0,0]+y[1,0]+y[2,0]==10)
constraints.append(y[0,1]+y[1,1]+y[2,1]==6)
constraints.append(y[0,0]+y[0,1]<=7*x[0,0])
constraints.append(y[1,0]+y[1,1]<=8*x[1,0])
constraints.append(y[2,0]+y[2,1]<=9*x[2,0])

obj_func=y[0,0]+6*y[0,1]+2*y[1,0]+5*y[1,1]+3*y[2,0]+4*y[2,1]-(8*x[0,0]+9*x[1,0]+7*x[2,0])

problem = cp.Problem(cp.Maximize(obj_func), constraints)
problem.solve()
print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)
print("y =")
print(y.value)
