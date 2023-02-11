import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# load data
squats_list = pickle.load(open("s.p", 'rb')) 

# function that only intepolate one row
def row_intepolated(squats_list):
    N=40 
    selected_row_of_all_squats=[]
    for i in range(len(squats_list)): 
        selected_row=squats_list[i][26,:]  # single row of a squat
        t=np.r_[0:squats_list[i].shape[1]] # row-wise merging
        # print(t[-1])
        t1 = x1 = np.linspace(0, squats_list[i].shape[1] - 1, N, endpoint=True) # specify 40 frames for each squat
        f = interp1d(t, selected_row,'cubic')
        selected_row_interp = f(t1)
        selected_row_of_all_squats.append(selected_row_interp)
        plt.plot(t, selected_row,'o',label="original")
        plt.plot(t1, selected_row_interp, 'x',label="inteperlated")
        plt.legend()
        plt.show()

# function that intepolates whole squat
def Intepolate_all_squats(squats_list):      
    N=40 
    intepolated_squats_list=[]
    for i in range(len(squats_list)): 
        single_squat = np.zeros((36, N)) # allocate an array of every intepolated squat
        t = np.r_[0:squats_list[i].shape[1]]
        t1 = x1 = np.linspace(0, squats_list[i].shape[1] - 1, N, endpoint=True)
        for j in range(0, squats_list[i].shape[0]): 
            f = interp1d(t, squats_list[i][j, :], 'cubic') 
            single_squat[j, :] = f(t1)
        intepolated_squats_list.append(single_squat)
    return intepolated_squats_list

def reconstruct_to_one_matrix(intepolated_squats_list):
    big_matrix= np.zeros((36*40,296))
    for i in range(len(intepolated_squats_list)):
        single_flat_squat=intepolated_squats_list[i].flatten()
        print(len(single_flat_squat))
        big_matrix[:,i] = single_flat_squat
    return big_matrix
    



intepolated_squats_list=Intepolate_all_squats(squats_list)
final_big_matrix=reconstruct_to_one_matrix(intepolated_squats_list)

# make sure the intepolated squat list has right shape 
for i in range(len(intepolated_squats_list)):
    if intepolated_squats_list[i].shape[0]!=36 or intepolated_squats_list[i].shape[1]!=40 :
        print("{a}th squat has wrong shape".format(a=i))
    else:
        print("squat {a} is an intepolated array of shape 36x40".format(a=i))

print("Final big matrix has the shape :",final_big_matrix.shape) #36*40
        


