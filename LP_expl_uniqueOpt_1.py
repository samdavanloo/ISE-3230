#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 09:25:11 2019

@author: Sam
"""

#%%
from pulp import *
pulp.pulpTestAll() # testing pulp

#%%
prob = LpProblem("expl_unique_optimal",LpMaximize) # create an LP maximization problem
x_1 = LpVariable("x_1",lowBound=0) # create a variable x_A>=0
x_2 = LpVariable("x_2",lowBound=0) # create a variable x_B>=0
prob += 2*x_1 + 3*x_2 # objective function
prob += x_1-2*x_2 <= 4 # contractual commitement
prob += 2*x_1 + x_2 <= 18 # assembly hours
prob += x_2 <= 10 # testing hours
prob # display the LP problem
#%%
status = prob.solve() # solve with default solver
LpStatus[status] # print the solution status
#%%
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("Total Cost = ", value(prob.objective))

#%%
# Solving the same problem in CVX (vector mode)
# Form: min c^Tx s.t. Ax<=b
from cvxopt import matrix, solvers
c=matrix([-2.0,-3.0])
A=matrix([[1.0,2.0,0.0,-1.0,0.0],[-2.0,1.0,1.0,0.0,-1.0]])
b=matrix([4.0,18.0,10.0,0.0,0.0])
sol=solvers.lp(c,A,b)
print(sol['x'])

#%%
# Solving the same problem in CVX
from cvxopt.modeling import variable,op
x_1 = variable()
x_2 = variable()
c1 = ( x_1-2*x_2 <= 4 )
c2 = ( 2*x_1+x_2 <= 18 )
c3 = ( x_2 <= 10 )
c4 = ( x_1>=0 )
c5 = ( x_2>=0 )
lp1 = op(-2*x_1-3*x_2, [c1,c2,c3,c4,c5])
lp1.solve()
lp1.status
print(x_1.value)
print(x_2.value)
print(lp1.objective.value())
print(c1.multiplier.value)
print(c2.multiplier.value)
print(c3.multiplier.value)
print(c4.multiplier.value)
print(c5.multiplier.value)

