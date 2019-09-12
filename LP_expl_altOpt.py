#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:59:11 2019

@author: Sam
"""
#%% Implementation in CVXOPT
from cvxopt.modeling import variable,op
x_1 = variable()
x_2 = variable()
c1 = ( 2*x_1+x_2 <= 16 )
c2 = ( x_1+x_2 <= 10 )
c3 = ( x_1>=0 )
c4 = ( x_2>=0 )
lp1 = op(-6*x_1-3*x_2, [c1,c2,c3,c4])
lp1.solve()
lp1.status
print(x_1.value)
print(x_2.value)
print(lp1.objective.value())
print(c1.multiplier.value)
print(c2.multiplier.value)
print(c3.multiplier.value)
print(c4.multiplier.value)


#%% Implementation in PULP
from pulp import *
pulp.pulpTestAll() # testing pulp

prob = LpProblem("expl_alt_optimal",LpMaximize) # create an LP maximization problem
x_1 = LpVariable("x_1",lowBound=0) 
x_2 = LpVariable("x_2",lowBound=0)
prob += 6*x_1 + 3*x_2 # objective function
prob += 2*x_1+x_2 <= 16 
prob += x_1 + x_2 <= 10
prob # display the LP problem
status = prob.solve() # solve with default solver
LpStatus[status]   # PULP also doesn NOT report existence of alternative optimal 

for v in prob.variables():
    print(v.name, "=", v.varValue)
print("Total Cost = ", value(prob.objective))