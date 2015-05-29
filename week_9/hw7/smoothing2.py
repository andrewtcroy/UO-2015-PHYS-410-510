import numpy as np
import matplotlib.pyplot as plt
from linearplus import linearplus as lp
import random
import math
from _future_ import division
data = np.genfromtxt("data.csv", delimiter=',')
time = [i[0] for i in data]
value = [i[1] for i in data]
#for i in data: 
#   time += [i[0]]

#graph, = plt.plot(time, value)
#plt.title("Unsmoothed Raw Data")

bxsmoothdata = [np.mean(value[i:i+5]) for i in range(len(data)-5)]
time = [i+5 for i in range(len(data)-5)]

chisquared = 0

for t in time:
	m = random.uniform(1, 10)
	a = random.uniform(1, 10)
	b = random.uniform(1, 10)
	w = random.uniform(1, 10)
	phi = random.uniform(1, 10)

	model = lp(t,m,a,b,w,phi)

chisquared = math.pow((value[t] - model[t]),2) / model[t]




graph2 = plt.plot(time, bxsmoothdata)
plt.title("BOXsmoothed by 5 Data")
plt.grid(True)
plt.show()

