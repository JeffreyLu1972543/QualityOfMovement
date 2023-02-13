import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

big_matrix = pickle.load(open("big_matrix.p", 'rb')) 



def offset_normalization(big_matrix):
    normalized_matrix=np.zeros((big_matrix.shape[0],big_matrix.shape[1]))
    # n=int(big_matrix.shape[0]/40)# 1440/40=36
    # print(n)
    for i in range(big_matrix.shape[1]):
        single_squat=big_matrix[:,i].reshape(36,40)
        single_squat_x=single_squat[0:18,:]
        single_squat_y=single_squat[18:36,:]
        for j in range(single_squat_x.shape[1]): #40
            origin_x=single_squat_x[10][j]
            origin_y=single_squat_y[10][j]
            single_squat_x[:,j]=single_squat_x[:,j]-origin_x
            single_squat_y[:,j]=single_squat_y[:,j]-origin_y
        single_flat_squat=(np.concatenate((single_squat_x,single_squat_y),axis=0)).flatten()
        normalized_matrix[:,i] = single_flat_squat
    return normalized_matrix

def check_correctness(normalized_matrix):
    list=[]
    for i in range(40):
        a=np.allclose(normalized_matrix[0+i*36:10+i*36,:],big_matrix[0+i*36:10+i*36,:])
        b=np.allclose(normalized_matrix[11+i*36:18+i*36,:],big_matrix[11+i*36:18+i*36,:])
        c=np.allclose(normalized_matrix[18+i*36:27+i*36,:],big_matrix[18+i*36:27+i*36,:])
        d=np.allclose(normalized_matrix[27+i*36:36+i*36,:],big_matrix[27+i*36:36+i*36,:])
        list.append(a&b&c&d)
    print(big_matrix[10,0])
    if ("False" in list)!=True:
        print("normalized_matrix is correct!")


normalized_matrix=offset_normalization(big_matrix)
check_correctness(normalized_matrix)

fw=open('normalized_matrix.p', 'wb')
pickle.dump(normalized_matrix, fw) 
fw.close()



