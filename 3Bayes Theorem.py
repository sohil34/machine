# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 07:58:38 2023

@author: saksh
"""

def drug_user(
        prob_th=0.8,
        sensitivity=0.79,
        specificity=0.79,
        prevelance=0.02,
        verbose=True):
#Computes the posterior using Bayes' rule
     p_user= prevelance
     p_non_user = 1-prevelance
     p_pos_user= sensitivity
     p_neg_user = specificity
     p_pos_non_user = 1-specificity
     num= p_pos_user*p_user
     den = p_pos_user*p_user+p_pos_non_user*p_non_user
     prob = num/den
     if verbose:
        if prob> prob_th:
            print("The test-taker could be an user")
        
        else:
           print("The test-taker may not be an user")
     return prob
p=drug_user(prob_th=0.5, sensitivity=0.97, specificity=0.95, prevelance=0.005)
print("Probability of the test-taker being a drug user is:", round(p,3)) 
