import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

squats_list = pickle.load(open("s.p", 'rb')) 

def row_intepolated(squats_list):
    N=40 
    selected_row_of_all_squats=[]
    for i in range(len(squats_list)): #Loop Through a List
        selected_row=squats_list[i][26,:]  # 第一个横行，第一个squat
        t=np.r_[0:squats_list[i].shape[1]] # row-wise merging
        # print(t[-1])
        t1 = x1 = np.linspace(0, squats_list[i].shape[1] - 1, N, endpoint=True) #不管有多少个frame 就取50个
        f = interp1d(t, selected_row,'cubic')
        selected_row_interp = f(t1)#这个f是个啥类型？
        selected_row_of_all_squats.append(selected_row_interp)
        # u=u+1
        # print("\n",u)
        # plt.plot(t, selected_row, 'o', t1, selected_row_interp, 'x')
        plt.plot(t, selected_row,'o',label="original")
        plt.plot(t1, selected_row_interp, 'x',label="inteperlated")
        plt.legend()
        plt.show()

def Intepolate_all_squats(squats_list):      
    N=40 
    C_all=[]
    for i in range(len(squats_list)): #每个squat
        # Now let's interpolate whole Squat
        C = np.zeros((36, N))
        t = np.r_[0:squats_list[i].shape[1]]
        t1 = x1 = np.linspace(0, squats_list[i].shape[1] - 1, N, endpoint=True)
        for j in range(0, squats_list[i].shape[0]): #每一行
            f = interp1d(t, squats_list[i][j, :], 'cubic') 
            C[j, :] = f(t1)#按行一起赋值
        C_all.append(C)
    return C_all

def reconstruct_to_one_matrix(intepolated_squats_list):
    big_matrix= np.zeros((36*40,296))
    for i in range(len(intepolated_squats_list)):
        single_flat_squat=intepolated_squats_list[i].flatten()
        print(len(single_flat_squat))
        big_matrix[:,i] = single_flat_squat
    print(big_matrix.shape)
    return big_matrix
    
# row_intepolated(squats_list)
intepolated_squats_list=Intepolate_all_squats(squats_list)
for i in range(len(intepolated_squats_list)):
    if intepolated_squats_list[i].shape[0]!=36 or intepolated_squats_list[i].shape[1]!=40 :
        print("{a}th squat has wrong shape".format(a=i))
    else:
        print("squat {a} is an intepolated array of shape 36x40".format(a=i))
        
reconstruct_to_one_matrix(intepolated_squats_list)


