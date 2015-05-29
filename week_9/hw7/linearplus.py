import numpy as np
import matplotlib.pyplot as plt
import random 
import math
def linearplus(t,m,b,a,w,phi):
	return m*t + b + a*math.sin(w*t + phi)
