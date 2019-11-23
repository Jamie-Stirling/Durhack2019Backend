import pandas as pd
import numpy as np
import scipy as sp

#inflation = 1
#nom_rate = 5
#n_years = 4
#annual_amount = 10

#cash_flow = [annual_amount for i in range(n_years)]

# real to nominal
def real_to_nom(real_rate, inflation):
    r = real_rate/100
    i = inflation/100
    n = (1+r)*(1+i)-1
    return n*100

# nominal to real
def nom_to_real(nom_rate, inflation):
    n = nom_rate/100
    i = inflation/100
    r = ((1+n)/(1+i))-1
    return r*100


# function to calculate future values taken into account of inflation
def FV(cash_flow, inflation, nom_rate):
    real_rate = nom_to_real(nom_rate, inflation)
    total = 0
    for i in cash_flow[:-1]:
        total = (total + i)*(1+real_rate/100)
    total += cash_flow[-1]

    total_saved = sum(cash_flow)
    total_worth = total
    passive_income = (real_rate/100)*total
    return (total_saved, total_worth, passive_income)

#future_value = FV(cash_flow, inflation, nom_rate)[1]
#print(future_value)

# function to calculate real rate of return
def REAL_RATE_NEEDED(cash_flow, future_value):
    coeff = cash_flow
    coeff[-1] = coeff[-1] - future_value
    for i in np.roots(coeff):
        if (np.imag(i) < 0.00001) and (np.real(i) >= 0):
            solution = (np.real(i)-1)*100
        else:
            solution = 'none'
    return solution

#print (REAL_RATE_NEEDED([0,10,10,10], 31.2037))



######################

class USER:
    def __init__(self, retireTarget, savingsTarget, timeToRetirement, currentPot):
        self.retireTarget = retireTarget
        self.savingsTarget = savingsTarget
        self.timeToRetirement = timeToRetirement
        self.currentPot = currentPot
        self.cashFlow = [self.currentPot]+[self.savingsTarget for i in range(self.timeToRetirement)]



#Mike = USER(100,10,3,0)

#print (FV(Mike.cashFlow, 1, 5))

#print (REAL_RATE_NEEDED(Mike.cashFlow, 31.2038))
