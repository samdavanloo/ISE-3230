#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:22:18 2019

@author: Sam

Solving the HiTech problem in PuLP

"""
#import sys   
#sys.modules[__name__].__dict__.clear()

#%%
clear()
from pulp import *
pulp.pulpTestAll() # testing pulp

#%%
prob = LpProblem("HiTech",LpMaximize) # create an LP maximization problem
x_A = LpVariable("x_A",lowBound=0) # create a variable x_A>=0
x_B = LpVariable("x_B",lowBound=0) # create a variable x_B>=0
prob += 20*x_A + 30*x_B # objective function
prob += x_A >= 25 # contractual commitement
prob += 4*x_A + 3*x_B <= 240 # assembly hours
prob += 1*x_A + 2*x_B <= 140 # testing hours
prob # display the LP problem
#%%
status = prob.solve() # solve with default solver
LpStatus[status] # print the solution status
#%%
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("Total Cost = ", value(prob.objective))
