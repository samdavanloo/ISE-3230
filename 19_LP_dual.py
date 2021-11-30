#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 08:01:30 2020


Problem Set 4.3B: Q3 (Taha Book, page 158)

@author: Sam
""" 

import cvxpy as cp

x = cp.Variable(4)

obj_func = 3*x[0]+6*x[1]+5*x[2]+4*x[3]

constraints = []
constraints.append(2*x[0]+5*x[1]+3*x[2]+4*x[3]<=5300) # Lathes
constraints.append(3*x[0]+4*x[1]+6*x[2]+4*x[3]<=5300) # Machine presses
constraints.append(x[0]>=0)
constraints.append(x[1]>=0)
constraints.append(x[2]>=0)
constraints.append(x[3]>=0)


problem = cp.Problem(cp.Maximize(obj_func), constraints)

problem.solve(solver=cp.GUROBI, verbose = True)
#problem.solve()

print("obj_func =", obj_func.value)
print("x =", x.value)

# Shadow prices or dual prices
print("dual variable for (2*x[0]+5*x[1]+3*x[2]+4*x[4]<=5300) ", constraints[0].dual_value)
print("dual variable for (3*x[0]+4*x[1]+6*x[2]+4*x[4]<=5300) ", constraints[1].dual_value)

# Reduced costs
print("reduced cost of the 1st primal variable x[0] ", constraints[2].dual_value)
print("reduced cost of the 2nd primal variable x[1] ", constraints[3].dual_value)
print("reduced cost of the 2nd primal variable x[2] ", constraints[4].dual_value)
print("reduced cost of the 2nd primal variable x[3] ", constraints[5].dual_value)

# Note that if the problem was minimization in the cacinical form, to get the reduced costs
# we had to multiply the dual values by -1.