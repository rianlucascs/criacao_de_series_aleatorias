
from random import choice
from numpy import sqrt
from random import randint
from yfinance import download

def rand():
    x1 = randint(-1, 1)
    if not(x1 == -1 or x1 == 1):
        while True:
            x2 = randint(-1, 1)
            if x2 == -1 or x2 == 1:
                return x2
    return x1  

def synthetic_data_generator(ticker,
                             number_of_days=240,
                             static_number_m=1,
                             static_number_s=1,
                             dynamic_number_a=[-100, -50, 0, 50, 100]):

    dynamic_number_b = list(range(len(dynamic_number_a)))
    
    s = 1
    p = float(download(ticker, period='1d', progress=False)[['Adj Close']].values[-1][0])
    list_data = []
    for _ in range(number_of_days):
        i = choice(dynamic_number_b)
        m = static_number_m / dynamic_number_a[i]
        s = static_number_s / dynamic_number_a[i]
        P = p + p * (m / number_of_days + s / sqrt(number_of_days) * rand())
        p = P
        s = P
        s += 1
        list_data.append(s)

    return list_data
