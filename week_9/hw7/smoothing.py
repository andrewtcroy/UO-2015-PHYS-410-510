import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data.csv", delimiter=',')
time = [i[0] for i in data]

time = [i[0] for i in data]
value = [i[1] for i in data]

#for i in data: 
#   time += [i[0]]

graph, = plt.plot(time, value)
plt.show()

