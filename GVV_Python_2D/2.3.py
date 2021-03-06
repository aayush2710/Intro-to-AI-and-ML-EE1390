#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 18:36:12 2019

@author: aayush
"""

import numpy as np

def mid_pt(B,C):
    D = (B+C)/2
    return D

def norm_vec(AB):
    return np.matmul(omat,np.matmul(AB,dvec))

def line_intersect(AD,CF):
    n1 = norm_vec(AD)
    n2=norm_vec(CF)
    N=np.vstack((n1,n2))
    p=np.zeros(2)
    p[0] = np.matmul(n1,AD[:,0])
    p[1] = np.matmul(n2,AD[:,0])
    return np.matmul(np.linalg.inv(N),p)

A = np.array([-2,-2])
B = np.array([1,3])
C=np.array([4,-1])
D = mid_pt(B,C)
F = mid_pt(A,B)
E = mid_pt(A,C)

AD = np.vstack((A,D)).T
CF = np.vstack((C,F)).T
BE = np.vstack((B,E)).T
dvec = np.array([-1,1])
omat= np.array([[0,1],[-1,0]])
Q = line_intersect(CF,BE)
print(Q[0])
