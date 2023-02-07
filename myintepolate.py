import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

squats_list = pickle.load(open("s.p", 'rb')) 

def row_intepolated(squats_list):
    N=50 
    row_0_all=[]
    for i in range(len(squats_list)): #Loop Through a List
        row_0=squats_list[i][26,:]  # 第一个横行，第一个squat
        t=np.r_[0:squats_list[i].shape[1]] # row-wise merging
        # print(t[-1])
        t1 = x1 = np.linspace(0, squats_list[i].shape[1] - 1, N, endpoint=True)#不管有多少个frame 就取50个
        f = interp1d(t, row_0,'cubic')
        row_0_interp = f(t1)
        row_0_all.append(row_0_interp)
        # u=u+1
        # print("\n",u)
        plt.plot(t, row_0, 'o', t1, row_0_interp, 'x')
        plt.show()

def Intepolate_all_squats(squats_list):      
    N=50 
    C_all=[]
    for i in range(len(squats_list)):
        # Now let's interpolate whole Squat
        C = np.zeros((36, N))
        t = np.r_[0:squats_list[i].shape[1]]
        t1 = x1 = np.linspace(0, squats_list[i].shape[1] - 1, N, endpoint=True)
        for j in range(0, squats_list[i].shape[0]):
            f = interp1d(t, squats_list[i][j, :], 'cubic')
            row_0_interp = f(t1)
            C[j, :] = f(t1)
        C_all.append(C)
    #plot_squat(C)

row_intepolated(squats_list)
