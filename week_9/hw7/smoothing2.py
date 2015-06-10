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

#print(len(bxsmoothdata))
#print(len(time))
#print((time))

frontmodels = []

for i in range(10000):
	m = random.uniform(2, 3 )
	a = random.uniform(300, 400)
	b = random.uniform(7500, 7600)
	w = random.uniform(2*math.pi/50, (2*math.pi)/100)
	phi = random.uniform(0, 2*math.pi)

	frontmodels += [[0,m,b,a,w,phi]]
	
	for t in time[0:600]:
		model = lp(t,m,a,b,w,phi)
		frontmodels[i][0] += ((math.pow((bxsmoothdata[t-5] - model),2)) / model)

backmodels = []

for i in range(1000):
	m = random.uniform(-3, 0)
	a = random.uniform(500, 600)
	b = random.uniform(9500, 10100)
	w = random.uniform(2*math.pi/10, (2*math.pi)/100)
	phi = random.uniform(0, 3)

	backmodels += [[0,m,b,a,w,phi]]
	
	for t in time[601:997]:
		model = lp(t,m,a,b,w,phi)
		backmodels[i][0] += ((math.pow((bxsmoothdata[t-5] - model),2)) / model)

#print(models)

bestfitval = 1000000000000000
bestfitfrontmodel = []
bestfitbackmodel = []

for model in frontmodels:
	if model[0] < bestfitval:
		bestfitval = model[0]
		bestfitfrontmodel = model

bestfitval = 1000000000000000

for model in backmodels:
	if model[0] < bestfitval:
		bestfitval = model[0]
		bestfitbackmodel = model

graph2 = plt.plot(time, bxsmoothdata)
plt.title("BOXsmoothed by 5 Data")
plt.grid(True)


plt.plot(time[0:600],[lp(t,bestfitfrontmodel[1], bestfitfrontmodel[2], bestfitfrontmodel[3], bestfitfrontmodel[4], bestfitfrontmodel[5]) for t in time[0:600]])
plt.plot(time[601:997],[lp(t,bestfitbackmodel[1], bestfitbackmodel[2], bestfitbackmodel[3], bestfitbackmodel[4], bestfitbackmodel[5]) for t in time[601:997]])
print(t,bestfitfrontmodel[1], bestfitfrontmodel[2], bestfitfrontmodel[3], bestfitfrontmodel[4], bestfitfrontmodel[5])
print(t,bestfitbackmodel[1], bestfitbackmodel[2], bestfitbackmodel[3], bestfitbackmodel[4], bestfitbackmodel[5])
plt.show()

