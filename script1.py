# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 20:31:24 2015

@author: xiaomu
"""

def addmultiply(dictA, dictB):
    dictC = {}
    for keyA in dictA.keys():
        for keyB in dictB.keys():
            dictC[keyA+keyB] =0
    for keyA, valueA in dictA.iteritems():
        for keyB, valueB in dictB.iteritems():
            dictC[keyA+keyB] = dictC[keyA+keyB] + valueA*valueB
    return dictC

def multiply(floatA, dictA):
    dictC = {}
    for keyA, valueA in dictA.iteritems():
        dictC[keyA] = valueA * floatA
    return dictC

def add(x, y):  
    return { k: x.get(k, 0) + y.get(k, 0) for k in set(x) | set(y) }

def checkdict(dictA):
    sum = 0
    for keyA, valueA in dictA.iteritems():
        sum = valueA + sum
    return sum


import numpy as np
import json

N = 50000    
f = {}
for i in range(N):
    f[i] = 0

f[0] = {1:1}
f[1] = {1:1}
f[2] = {2:2/float(3), 1:1/float(3)}
f[3] = {2:1}
f[4] = {3:7/float(15), 2:8/float(15)} 
for i in range(5,N):
    sum_f = {}
    for j in range(3, i):
        sum_f = add(sum_f, addmultiply(f[j-2-1], f[i-j-1]))
    sum_f = multiply(1/float(i+1), sum_f)
    f[i] = addmultiply(add(add(multiply(2/float(i+1), f[i-3]),  multiply(2/float(i+1), f[i-2])),sum_f), f[0])
    if np.mod(i, 500) == 5:
        print i    

dictA = f[N-1]
with open('./data_v2.json', 'wb') as fp:
    json.dump(dictA, fp)


#expectation = 0
#for keyA, valueA in dictA.iteritems():
#    expectation = expectation + dictA[keyA]*keyA
#print expectation
#variance = 0
#for keyA, valueA in dictA.iteritems():
#    variance = variance+np.square(keyA - expectation)*dictA[keyA]
#print variance
    
