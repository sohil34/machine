# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 20:07:21 2023

@author: saksh
"""

from random import randint 
TRAIN_SET_LIMIT=1000 
TRAIN_SET_COUNT=100 
TRAIN_INPUT = list() 
TRAIN_OUTPUT = list()
for i in range (TRAIN_SET_COUNT) : 
    a = randint(0, TRAIN_SET_LIMIT ) 
    b = randint(0, TRAIN_SET_LIMIT ) 
    c = randint(0, TRAIN_SET_LIMIT ) 
    op = a + (2 * b) + (3 * c) 
    TRAIN_INPUT.append([a ,b, c]) 
    TRAIN_OUTPUT.append(op)
from sklearn.linear_model import LinearRegression 
predictor = LinearRegression(n_jobs =-1) 
predictor.fit(X = TRAIN_INPUT , y = TRAIN_OUTPUT) 
X_Test =[[20 ,40,60]]
outcome = predictor.predict(X = X_Test) 
coefficients = predictor.coef_
print('Outcome : {} \nCoefficients : {}'.format( outcome ,coefficients))
