import numpy as np
import matplotlib.pyplot as plt
from linearplus import linearplus as lp
import random
import math

data = np.genfromtxt("data.csv", delimiter=',')
time = [i[0] for i in data]
value = [i[1] for i in data]

bxsmoothdata = [np.mean(value[i:i+5]) for i in range(len(data)-5)]
time = [i+5 for i in range(len(data)-5)]

graph2 = plt.plot(time, bxsmoothdata)
plt.title("BOXsmoothed by 5 Data")
plt.grid(True)
plt.show()
