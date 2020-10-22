#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:57:16 2020

@author: Sam
"""

import cvxpy as cp

x = cp.Variable(3, boolean = True)


obj_func = 10*x[0]+12*x[1]+13*x[2]

constraints = []
constraints.append(x[0]+x[2]>=1)
constraints.append(x[1]>=1)
constraints.append(x[0]+x[1]>=1)
constraints.append(x[2]>=1)

problem = cp.Problem(cp.Minimize(obj_func), constraints)

problem.solve(solver=cp.GUROBI, verbose = True)

print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)