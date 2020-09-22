#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:23:55 2020

CVXPY code for the LP investment example.

@author: Sam
"""

import cvxpy as cp

x = cp.Variable(5, nonneg  = True) # vector variable
s = cp.Variable(3, nonneg  = True) # vector variable

obj_func=x[1]+1.9*x[3]+1.5*x[4]+1.08*s[2]

constraints = []
constraints.append(x[0]+x[2]+x[3]+s[0]==100000)
constraints.append(0.5*x[0]-x[1]+1.2*x[2]+1.08*s[0]-s[1]==0)
constraints.append(x[0]+0.5*x[1]-x[4]+1.08*s[1]-s[2]==0)
constraints.append(x[0]<=75000)
constraints.append(x[1]<=75000)
constraints.append(x[2]<=75000)
constraints.append(x[3]<=75000)
constraints.append(x[4]<=75000)


problem = cp.Problem(cp.Maximize(obj_func), constraints)

#problem.solve(solver=cp.CVXOPT,verbose = True)
problem.solve(solver=cp.GUROBI,verbose = True)

print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)
print("s =")
print(s.value)
