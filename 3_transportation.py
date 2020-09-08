#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 12:12:13 2020

CVXPY code for the LP transportation example.

@author: Sam
"""

import cvxpy as cp
import numpy as np


X = cp.Variable((3, 4), nonneg  = True)
m,n=X.shape

C=np.array([[7,3,8,4],[9,5,6,3],[4,6,9,6]]) # unit shipping costs  (3*4 matrix)
W=np.array([[6000],[9000],[4000]])          # warehouse availabiliy (column vector)
R=np.array([[3900,5200,2700,6400]])         # retail outlet demand (row vector)

obj_func=cp.trace(C.T @ X)  #.T takes transpose of a matrix, @ represents matrix product, trace sums the diagonal elements

#%% 1. Inputing constraints using two for loops for columns and rows

constraints = []
for j in range(n):
    constraints.append(cp.sum(X[:,j], axis=0, keepdims=True)==R[0,j]) # axis=0 sums over rows for each column

for i in range(m):
    #constraints.append(cp.sum(X[i,:], axis=1)<=W[i]) # axis=1 sums over columns for each row
    #Ethan Lynagh: The error is the axis=1 in cp.sum, code runs fine when you remove it
    constraints.append(X[i,0]+X[i,1]+X[i,2]+X[i,3]<=W[i])
    
problem = cp.Problem(cp.Minimize(obj_func), constraints)
problem.solve(solver=cp.CVXOPT,verbose = True)

print("obj_func =")
print(obj_func.value)
print("X =")
print(np.round(X.value)) 
    
#%% 2. Inputing constraints using vector operation

constraints = []
col_sums = cp.sum(X, axis=0, keepdims=True) # axis=0 sums over rows for each column
constraints.append(col_sums==R)
row_sums = cp.sum(X, axis=1, keepdims=True) # axis=1 sums over columns for each row
constraints.append(row_sums<=W)

problem = cp.Problem(cp.Minimize(obj_func), constraints)
problem.solve(solver=cp.CVXOPT,verbose = True)

print("obj_func =")
print(obj_func.value)
print("X =")
print(X.value)   


 