import scipy
import numpy as np
from scipy import integrate
import pandas as pd


def f(x):
    return np.log(x)

g = integrate.quad(f, 0, 1)
print(g)

df = pd.DataFrame({'A': [1, 2, 3, 1, -1], 'B': [4, 5, 6, -3, -2.3]})
print(df.rolling(2).mean())


s = pd.Series([1, -100, 200, 0, 100])

print(s.rolling(window=2).mean())
