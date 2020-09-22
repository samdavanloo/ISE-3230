#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:31:43 2020

CVXPY code for the LP product blend example.

@author: Sam
"""
import cvxpy as cp


X = cp.Variable((2, 2), nonneg  = True)
#m,n=X.shape


obj_func=15*X[0,0]+20*X[0,1]+11*X[1,0]+16*X[1,1]


constraints = []
constraints.append(-X[0,0]+9*X[1,0]>=0)
constraints.append(-7*X[0,1]+3*X[1,1]>=0)
constraints.append(X[0,0]+X[1,0]>=60000)
constraints.append(X[0,1]+X[1,1]>=15000)
constraints.append(X[0,0]+X[1,0]<=80000)
constraints.append(X[0,1]+X[1,1]<=40000)
constraints.append(X[0,0]+X[0,1]<=70000)
constraints.append(X[1,0]+X[1,1]<=60000)


problem = cp.Problem(cp.Maximize(obj_func), constraints)

problem.solve(solver=cp.CVXOPT,verbose = True) #verbose parameter determines showing/not showing the output
#problem.solve(solver=cp.GUROBI,verbose = True)

print("obj_func =")
print(obj_func.value)
print("X =")
print(X.value)
