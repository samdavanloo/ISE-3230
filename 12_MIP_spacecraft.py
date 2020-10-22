#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 09:39:46 2020

@author: Sam
"""

import cvxpy as cp

x = cp.Variable(2, integer = True)


obj_func=x[0]+x[1]

constraints = []
constraints.append(17*x[0]+32*x[1]<=136)
constraints.append(32*x[0]+15*x[1]<=120)
constraints.append(x[0]>=0)
constraints.append(x[1]>=0)


problem = cp.Problem(cp.Maximize(obj_func), constraints)

problem.solve(solver=cp.GUROBI,verbose = True)

print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)

