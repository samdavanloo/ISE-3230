#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:39:25 2020

@author: Sam
"""

import cvxpy as cp


x = cp.Variable(2, nonneg  = True) # vector variable


obj_func=6*x[0]+3*x[1]

constraints = []
constraints.append(2*x[0]+x[1]<=16)
constraints.append(x[0]+x[1]<=10)


problem = cp.Problem(cp.Maximize(obj_func), constraints)

#problem.solve(solver=cp.CVXOPT,verbose = True)
#problem.solve(verbose = True)
problem.solve(solver=cp.GUROBI,verbose = True) # good solver plays a role

print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)