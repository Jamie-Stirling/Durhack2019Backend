import datetime
import numpy as np


# inflation = 1
# nom_rate = 5
# n_years = 4
# annual_amount = 10

# cash_flow = [annual_amount for i in range(n_years)]

# real to nominal
def real_to_nom(real_rate, inflation):
    r = real_rate / 100
    i = inflation / 100
    n = (1 + r) * (1 + i) - 1
    return n * 100


# nominal to real
def nom_to_real(nom_rate, inflation):
    n = nom_rate / 100
    i = inflation / 100
    r = ((1 + n) / (1 + i)) - 1
    return r * 100


# function to calculate future values taken into account of inflation
def FV(cash_flow, inflation, nom_rate):
    real_rate = nom_to_real(nom_rate, inflation)
    total = 0
    totals = []

    for i in cash_flow[:-1]:
        total = (total + i) * (1 + real_rate / 100)
        totals.append(total)
    total += cash_flow[-1]
    totals.append(total)

    total_saved = sum(cash_flow)

    passive_income = (real_rate / 100) * total
    return total_saved, passive_income, totals


# future_value = FV(cash_flow, inflation, nom_rate)[1]
# print(future_value)

# function to calculate real rate of return
def REAL_RATE_NEEDED(cash_flow, future_value):
    coeff = cash_flow
    coeff[-1] = coeff[-1] - future_value
    solution = 0
    for i in np.roots(coeff):
        if (np.imag(i) < 0.00001) and (np.real(i) >= 0):
            solution = (np.real(i) - 1) * 100
        else:
            solution = 'none'
    return solution


class User:
    def __init__(self, retireTarget, savingsTarget, timeToRetirement, cashFlow):
        self.retireTarget = retireTarget
        self.savingsTarget = savingsTarget
        self.timeToRetirement = timeToRetirement
        self.cashFlow = cashFlow


def handle_request(data):
    current_date = datetime.datetime.now()

    time_to_retire = data["retireTargetAge"]

    print(data, time_to_retire)

    def calc_cash_flow(t, max):
        if t < max / 2:
            j = 2 * t / max
            return data["salary"]["now"] * (1 - j) + j * data["salary"]["halfWay"]
        else:
            j = 2 * t / max - 1
            return data["salary"]["halfWay"] * (1 - j) + j * data["salary"]["retire"]

    cash_flow = [0] + [calc_cash_flow(i, time_to_retire) for i in range(time_to_retire)]

    user = User(0, data["savingsTarget"], time_to_retire, cash_flow)

    (total, passive_income, totals) = FV(user.cashFlow, 2.5, 2)
    rrr = REAL_RATE_NEEDED(user.cashFlow, 31.2038)

    data = {
        "totals": totals,
        "passive_income": passive_income,
        "rrr": rrr
    }

    return data
# print (REAL_RATE_NEEDED(Mike.cashFlow, 31.2038))

# Mike = USER(100,10,3,0)

# print (FV(Mike.cashFlow, 1, 5))

