#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:38:09 2019

@author: Sam
"""

import numpy as np
import cvxpy as cp

A = np.array([[17,32],[32,15]])
ones_vec = np.ones(A.shape[1])

x = cp.Variable(A.shape[1], integer = True) 

constraints = []
constraints.append(A[0,:] * x <= 136)
constraints.append(A[1,:] * x <= 120)
constraints.append(x >= 0)

obj_func=ones_vec*x

problem = cp.Problem(cp.Maximize(obj_func), constraints)
problem.solve()
print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)
