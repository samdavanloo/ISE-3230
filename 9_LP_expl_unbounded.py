#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:45:25 2020

@author: Sam
"""

import cvxpy as cp


x = cp.Variable(2, nonneg  = True) # vector variable


obj_func=x[0]+3*x[1]

constraints = []
constraints.append(x[0]-2*x[1]<=4)
constraints.append(-x[0]+x[1]<=3)
constraints.append(x[1]>=2)


problem = cp.Problem(cp.Maximize(obj_func), constraints)
#problem = cp.Problem(cp.Minimize(obj_func), constraints)

#problem.solve(solver=cp.CVXOPT,verbose = True)
#problem.solve(verbose = True)
problem.solve(solver=cp.GUROBI,verbose = True)

print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)