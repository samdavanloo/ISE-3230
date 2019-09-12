#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:47:40 2019

@author: Sam
"""
#%% Implementation in CVXOPT
from cvxopt.modeling import variable,op
x_1 = variable()
x_2 = variable()
c1 = ( x_1-2*x_2 <= 4 )
c2 = ( -x_1+x_2 <= 3 )
c3 = ( x_2 >= 2 )
c4 = ( x_1>=0 )
c5 = ( x_2>=0 )
lp1 = op(-x_1-3*x_2, [c1,c2,c3,c4,c5])
lp1.solve()
lp1.status
print(x_1.value)
print(x_2.value)
print(lp1.objective.value())

#%% Implementation in PULP
from pulp import *
pulp.pulpTestAll() # testing pulp

prob = LpProblem("expl_unbounded_optimal",LpMaximize) # create an LP maximization problem
x_1 = LpVariable("x_1",lowBound=0) 
x_2 = LpVariable("x_2",lowBound=0)
prob += x_1 + 3*x_2 # objective function
prob += x_1-2*x_2 <= 4 
prob += -x_1 + x_2 <= 3
prob += x_2 >= 2
prob # display the LP problem
status = prob.solve() # solve with default solver
LpStatus[status]   # PULP explicitly reports unboundedness
