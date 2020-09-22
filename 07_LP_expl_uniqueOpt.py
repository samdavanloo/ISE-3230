#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:40:40 2020

@author: Sam
"""

import cvxpy as cp


x = cp.Variable(2, nonneg  = True) # vector variable


obj_func=2*x[0]+3*x[1]
#obj_func_neg=-2*x[0]-3*x[1]

constraints = []
constraints.append(x[0]-2*x[1]<=4)
constraints.append(2*x[0]+x[1]<=18)
constraints.append(x[1]<=10)


problem = cp.Problem(cp.Maximize(obj_func), constraints)
#problem = cp.Problem(cp.Minimize(obj_func_neg), constraints)

#problem.solve(solver=cp.CVXOPT,verbose = True)
#problem.solve(verbose = True)
problem.solve(solver=cp.GUROBI,verbose = True)

print("obj_func =")
print(obj_func.value)
#print(obj_func_neg.value)
print("x =")
print(x.value)
