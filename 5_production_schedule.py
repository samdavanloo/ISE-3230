#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:10:29 2020

CVXPY code for the LP production schedule example.

@author: Sam
"""

import cvxpy as cp


x = cp.Variable(4, nonneg  = True) # vector variable
y = cp.Variable(2, nonneg  = True) # vector variable
w = cp.Variable(3, nonneg  = True) # vector variable


obj_func=12*x[0]+12*x[1]+14*x[2]+14*x[3]+16*y[0]+16*y[1]+3*(w[0]+w[1]+w[2])


constraints = []
constraints.append(x[0]-w[0]==400)
constraints.append(x[1]+y[0]+w[0]-w[1]==750)
constraints.append(x[2]+y[1]+w[1]-w[2]==950)
constraints.append(x[3]+w[2]==700)  # to fix infeasibility change 900 to 700
constraints.append(x[0]<=800)
constraints.append(x[1]<=800)
constraints.append(x[2]<=800)
constraints.append(x[3]<=800)
constraints.append(y[0]<=200)
constraints.append(y[1]<=200)
constraints.append(w[0]<=50)
constraints.append(w[1]<=50)
constraints.append(w[2]<=50)



problem = cp.Problem(cp.Minimize(obj_func), constraints)

#problem.solve(solver=cp.CVXOPT,verbose = True)
problem.solve(solver=cp.GUROBI,verbose = True)

print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)
print("y =")
print(y.value)
print("w =")
print(w.value)