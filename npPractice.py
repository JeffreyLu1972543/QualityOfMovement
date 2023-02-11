import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
# flatten
c=np.zeros((6,2))
x1 = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
x2 = np.array([[7, 8, 9], [10, 11, 12]], np.int32)
flat_x1=x1.flatten()
flat_x2=x2.flatten()
c[:,0]=flat_x1
c[:,1]=flat_x2
print(c.shape)
print(c)