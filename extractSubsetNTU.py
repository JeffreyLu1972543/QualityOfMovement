import os
from tkinter import E
import numpy as np
import json
import shutil
from scipy.interpolate import interp1d
import re
import struct
import pickle
# from plotNTUskeleton import *

ntu_path = '/Users/jeffreylu/Desktop/NTUdataset/nturgbd_skeletons_s001_to_s017/'
output_path = '/Users/jeffreylu/Desktop/NTUdataset/subset'

def num_files():
    folder_path = output_path # replace with the actual folder path
    num_files = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
    print("Total number of files in the folder:", num_files)    

def getSubset_NTU(ntu_path,output_path):
    # Set the subset of actions to extract
    setup_number="S001"
    camera_id="C001"
    subset_actions = [7,8,17,21,22,27] 
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    # Get a list of all the skeleton data files in the dataset
    skeleton_files = sorted([filename for filename in os.listdir(ntu_path) if filename.endswith('.skeleton')])

    for skeleton_file in skeleton_files:
        input_filename=os.path.join(ntu_path, skeleton_file)
        # Get the action label for the current data
        action_label = int(skeleton_file.split('A')[1][:3]) #S017C003P020R002A055.skeleton => 055
        if (action_label in subset_actions)and(skeleton_file.startswith(f'{setup_number}{camera_id}')): # 获取S001C001的actions
            output_filename = os.path.join(output_path, skeleton_file)
            shutil.copy(input_filename , output_path)

# 想办法把数据弄成  filenumber x 75 x whatever自己的frame
def extract_features_x(data_path):
    # Initialize lists for feature matrices and labels
    # num_frames = 0
    feature_matrices = []
    # Loop through all files in the data path
    for file_name in os.listdir(data_path):
        if file_name.endswith('.skeleton')==False:
            print("111!!!!!")
            print(file_name)
        if file_name.endswith('.skeleton'):
            # Extract x, y, z coordinates for all joints in all frames
            with open(os.path.join(data_path, file_name), 'r') as f:
                num_frames= int(f.readline())
                f.readline()
                f.readline()
                f.readline()
                data = f.read().split('\n')[:-1]
                data2=[]
                for k in range(len(data)):
                    if((len(data[k].split())>=11)):
                        # print(data[k])
                        data2.append(data[k])
                # print("#######",data[0])
                # print("{a} has {b} frames".format(a=file_name,b=num))
            num_joints = 25
            x = np.zeros((num_joints,num_frames))
            y = np.zeros((num_joints,num_frames))
            z = np.zeros((num_joints,num_frames))
            for i in range(num_frames):
                # frame_data = data[i*num_joints+i*3: (i+1)*num_joints+i*3]
                frame_data = data2[i*num_joints: (i+1)*num_joints]
                # print("len:",len(frame_data))
                for j in range(num_joints):
                    line = frame_data[j]
                    numbers = line.split()
                    first_three_numbers = numbers[:3]
                    if(len(first_three_numbers))!=3:
                        print(first_three_numbers[0])
                        print(file_name,num_frames)
                    # if(file_name=="S001C001P008R002A027.skeleton")and(i==0):
                    #     print(first_three_numbers)
                    # print(first_three_numbers)
                
                    x[j,i], y[j,i], z[j,i] = map(float, first_three_numbers)
                        # x[j,i]=first_three_numbers[0]
                        # y[j,i]=first_three_numbers[1]
                        # z[j,i]=first_three_numbers[2]
                        # print(x[j,i],y[j,i],z[j,i])

            # Construct feature matrix for this action
            features = np.concatenate((x, y, z), axis=0)
            feature_matrices.append(features)
    # Concatenate all feature matrices into a single matrix
    # feature_matrix = np.concatenate(feature_matrices)
    print("The length od feature matrix:",len(feature_matrices))
    # for m in range(len(feature_matrices)):
    #     print(feature_matrices[m].shape)
    return feature_matrices






def Intepolate_all_squats(squats_list):      
    N=206
    intepolated_squats_list=[]
    for i in range(len(squats_list)): 
        single_squat = np.zeros((75, N)) # allocate an array of every intepolated squat
        t = np.r_[0:squats_list[i].shape[1]]
        t1 = x1 = np.linspace(0, squats_list[i].shape[1] - 1, N, endpoint=True)
        for j in range(0, squats_list[i].shape[0]): 
            f = interp1d(t, squats_list[i][j, :], 'cubic') 
            single_squat[j, :] = f(t1)
        intepolated_squats_list.append(single_squat)
    return intepolated_squats_list

def reconstruct_to_one_matrix(intepolated_squats_list):
    N=206
    big_matrix= np.zeros((75*N,96))
    for i in range(len(intepolated_squats_list)):
        single_flat_squat=intepolated_squats_list[i].flatten()
        # print(len(single_flat_squat))
        big_matrix[:,i] = single_flat_squat
    return big_matrix

def get_class_labels(output_path):
    class_number= []
    # Iterate through all files in the folder
    for filename in os.listdir(output_path):
        if filename.endswith('.skeleton'):
            filename_no_extension=os.path.splitext(os.path.basename(filename))[0]
            last_3_chars = filename_no_extension[-3:]
            class_number.append(last_3_chars)
    print("The total number of labels",len(class_number))
    return class_number


# def spilt_dataset():
#     path = '/Users/jeffreylu/Desktop/NTUdataset/subset' # 文件夹目录，存放所有56880个样本的文件夹
#     training_path='/Users/jeffreylu/Desktop/NTUdataset/Cross-View-Train'
#     test_path='/Users/jeffreylu/Desktop/NTUdataset/Cross-View-Test'

#     files = os.listdir(path)    # 得到文件夹下的所有文件名称
#     train = ['C002', 'C003']
#     test = ['C001']
#     for file in files:  # 遍历文件夹
#         for i in range(2):
#             if train[i] in file:
#                 file = os.path.join(path, file)
#                 if not os.path.exists(training_path):
#                     os.makedirs(training_path)
#                 shutil.copy(file, training_path)
#         for i in range(1):
#             if test[i] in file:
#                 file = os.path.join(path,file)
#                 if not os.path.exists(test_path):
#                     os.makedirs(test_path)
#                 shutil.copy(file, test_path)
getSubset_NTU(ntu_path,output_path)
num_files()
action_labels=get_class_labels(output_path)
action_list=extract_features_x(output_path)
intepolated_list=Intepolate_all_squats(action_list)
big_action_matrix=reconstruct_to_one_matrix(intepolated_list)
print(big_action_matrix.shape)

fw=open('NTU_bigMatrix.p', 'wb')
pickle.dump(big_action_matrix, fw) 
fw.close()
fw=open('NTU_labels.p', 'wb')
pickle.dump(action_labels, fw) 
fw.close()


# spilt_dataset()
#-------------------------------------------------------------

