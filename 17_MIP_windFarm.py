#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:03:46 2020

@author: Sam
"""

import cvxpy as cp

x = cp.Variable((3,3), boolean = True)


obj_func = 10*x[0,0]+12*x[0,1]+14*x[0,2]\
            +9*x[1,0]+8*x[1,1]+15*x[1,2]\
            +10*x[2,0]+5*x[2,1]+15*x[2,2]
            
constraints = []
constraints.append(x[0,0]+x[0,1]+x[0,2]==1)
constraints.append(x[1,0]+x[1,1]+x[1,2]==1)
constraints.append(x[2,0]+x[2,1]+x[2,2]==1)
constraints.append(x[0,0]+x[1,0]+x[2,0]==1)
constraints.append(x[0,1]+x[1,1]+x[2,1]==1)
constraints.append(x[0,2]+x[1,2]+x[2,2]==1)


problem = cp.Problem(cp.Minimize(obj_func), constraints)

problem.solve(solver=cp.GUROBI, verbose = True)
#problem.solve()

print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)