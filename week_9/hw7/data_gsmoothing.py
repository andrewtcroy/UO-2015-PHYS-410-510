import numpy as np
import matplotlib.pyplot as plt

#read data into list
with open('data.csv') as f:
	List = f.read().splitlines()

# setup variable to measure length of list (number of elements)
listLength = len(List)

#turn the data file into a 2-dimensional list by using a 'for' loop
for i in range(listLength):
	List[i] = List[i].split()

array = np.zeros(2,1001)

for i in range(listLength):
	array.itemset(i,)


