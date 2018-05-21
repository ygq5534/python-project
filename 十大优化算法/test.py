
import numpy as np
import pandas as pd
from benchmark import Benchmark

fit = np.zeros((40,10))
xi = np.zeros(20)
x = pd.DataFrame(-1 + 2*np.random.rand(40,20))*100
test = Benchmark(20)
for i in np.arange(40):
    xi = x.iloc[i]
    fit[i] = test.Fitness(xi)
print(fit)