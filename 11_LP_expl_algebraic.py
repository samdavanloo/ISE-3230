#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:09:03 2020

@author: Sam
"""

import cvxpy as cp


x = cp.Variable(2, nonneg  = True) # vector variable

obj_func=x[0]+x[1]

constraints = []
constraints.append((2/3)*x[0]+x[1]<=18)
constraints.append(2*x[0]+x[1]>=8)
constraints.append(x[0]<=12)
constraints.append(x[1]<=16)

problem = cp.Problem(cp.Maximize(obj_func), constraints)

problem.solve(solver=cp.GUROBI,verbose = True)

print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)