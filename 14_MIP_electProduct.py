#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:04:19 2020

@author: Sam
"""

import cvxpy as cp

x = cp.Variable(3, boolean = True)
p = cp.Variable(3, nonneg = True)


obj_func = (2*p[0]+5*p[1]+p[2])+(40*x[0]+50*x[1]+35*x[2])

constraints = []
constraints.append(p[0]+p[1]+p[2]==50)
constraints.append(5*x[0]-p[0]<=0)
constraints.append(p[0]-20*x[0]<=0)
constraints.append(6*x[1]-p[1]<=0)
constraints.append(p[1]-40*x[1]<=0)
constraints.append(4*x[2]-p[2]<=0)
constraints.append(p[2]-35*x[2]<=0)

problem = cp.Problem(cp.Minimize(obj_func), constraints)

problem.solve(solver=cp.GUROBI, verbose = True)

print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)
print("p =")
print(p.value)