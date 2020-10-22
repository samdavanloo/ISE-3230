#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:17:49 2020

@author: Sam
"""

import cvxpy as cp

x = cp.Variable(2, boolean = True)
p = cp.Variable(2, nonneg = True)
f = cp.Variable(3, nonneg = True)


obj_func = (2*p[0]+3*p[1])-(50*x[0]+55*x[1])

constraints = []
constraints.append(p[0]-f[0]-f[2]==0)
constraints.append(p[1]-f[1]+f[2]==0)
constraints.append(f[0]+f[1]==30)
constraints.append(-f[2]<=10)
constraints.append(f[2]<=10)
constraints.append(f[0]-11*x[0]<=12)
constraints.append(f[1]-12*x[1]<=11)


problem = cp.Problem(cp.Maximize(obj_func), constraints)

problem.solve(solver=cp.GUROBI, verbose = True)

print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)
print("p =")
print(p.value)
print("f =")
print(f.value)