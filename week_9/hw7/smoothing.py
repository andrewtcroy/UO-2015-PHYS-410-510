import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data.csv", delimiter=',')
time = [i[0] for i in data]

time = [i[0] for i in data]
value = [i[1] for i in data]

#for i in data: 
#   time += [i[0]]

#graph, = plt.plot(time, value)
#plt.title("Unsmoothed Raw Data")

bxsmoothdata = [np.mean(value[i:i+5]) for i in range(len(data)-5)]
time = [i for i in range(len(data)-5)]

graph2 = plt.plot(time, bxsmoothdata)
plt.title("BOXsmoothed by 5 Data")
plt.show()