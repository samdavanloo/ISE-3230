#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 11:47:24 2020

CVXPY code for HiTech example.

@author: Sam
"""

import cvxpy as cp

x = cp.Variable(2, nonneg  = True) # vector variable

obj_func=20*x[0]+30*x[1]

constraints = []
constraints.append(x[0]>=25)
constraints.append(4*x[0]+3*x[1]<=240)
constraints.append(x[0]+2*x[1]<=140)

problem = cp.Problem(cp.Maximize(obj_func), constraints)

problem.solve(solver=cp.CVXOPT,verbose = True) #verbose parameter determines showing/not showing the output

print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)
