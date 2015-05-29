import numpy as np
import matplotlib.pyplot as plt
from linearplus import linearplus as lp
import random
import math

data = np.genfromtxt("data.csv", delimiter=',')
time = [i[0] for i in data]
value = [i[1] for i in data]
#for i in data: 
#   time += [i[0]]

#graph, = plt.plot(time, value)
#plt.title("Unsmoothed Raw Data")

bxsmoothdata = [np.mean(value[i:i+5]) for i in range(len(data)-5)]
time = [i+5 for i in range(len(data)-5)]

models = [[]]

for i in range(100):
	m = random.uniform(1, 10)
	a = random.uniform(1, 10)
	b = random.uniform(1, 10)
	w = random.uniform(1, 10)
	phi = random.uniform(1, 10)

	models += [0,m,b,a,w,phi]
	
	for t in time:
		model = lp(t,m,a,b,w,phi)
		print(models)
		models[i][0] += (math.pow((bxsmoothdata[t] - model),2) / model)

bestfitval = 1000
bestfitmodel = []

for model in models:
	if model[0] < bestfitval:
		bestfitval = model[0]
		bestfitmodel = model

graph2 = plt.plot(time, bxsmoothdata)
plt.title("BOXsmoothed by 5 Data")
plt.grid(True)
plt.show()

