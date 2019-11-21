#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:46:02 2019

@author: Sam Davanloo
"""

import cvxpy as cp


x = cp.Variable(2, nonneg  = True) # vector variabl

constraints = []
constraints.append(0.15*x[0]+0.2*x[1]<=200)
constraints.append(0.1*x[0]+0.2*x[1]<=140)
constraints.append(2.5*x[0]+4*x[1]<=3200)
constraints.append(x[0]<=900)
constraints.append(x[1]<=600)

obj_func=7*x[0]+12*x[1]

problem = cp.Problem(cp.Maximize(obj_func), constraints)
problem.solve(solver=cp.CVXOPT,verbose = True)
print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)


# Finding Shadow Prices
print("optimal (0.15x1 + 0.2x2 <= 200) dual variable", constraints[0].dual_value)
print("optimal (0.1x1 + 0.2x2 <= 140) dual variable", constraints[1].dual_value)
print("optimal (2.5x1 + 4x2 <= 3200) dual variable", constraints[2].dual_value)
print("optimal (x1 <= 900) dual variable", constraints[3].dual_value)
print("optimal (x2 <= 600) dual variable", constraints[4].dual_value)

# Finding Reduced Costs