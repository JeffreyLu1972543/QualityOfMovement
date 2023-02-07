import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

# Set the figure size
plt.rcParams["figure.figsize"]=[7.00, 3.50]
plt.rcParams["figure.autolayout"]=True
# Define the values
x = np.arange(0, 10) # np.arange(0,10,1)
# y=np.exp(x)
# e=2.718
y = np.exp(-x/5.0)  # e的多少次方
# print(y)

# Input Data
plt.subplot(1,2,1)
plt.title("Input X and Y")
plt.plot(x,y)

# Interpolated Data
plt.subplot(1,2,2)
plt.title("Interpolated")
f = interpolate.interp1d(x, y)
x_new = np.arange(0, 7, 0.7) #前开后闭
print(x_new)
y_new = f(x_new)
plt.plot(x_new, y_new, 's')

plt.show()
# t=np.r_[0:5]
# t1 = x1 = np.linspace(0, 10,3 , endpoint=True)
# t2 = x1 = np.linspace(0, 10,3 , endpoint=False)
# # print(t)
# print(t1)
# print(t2)