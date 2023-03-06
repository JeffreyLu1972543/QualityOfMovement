import os
import numpy as np
import json
import shutil

ntu_path = '/Users/jeffreylu/Desktop/NTUdataset/nturgbd_skeletons_s001_to_s017/'
output_path = '/Users/jeffreylu/Desktop/NTUdataset/subset'

def getSubset_NTU(ntu_path,output_path):
    # Set the subset of actions to extract
    subset_actions = [7,8,17,21,22,27,88] 
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    # Get a list of all the skeleton data files in the dataset
    skeleton_files = sorted([filename for filename in os.listdir(ntu_path) if filename.endswith('.skeleton')])

    for skeleton_file in skeleton_files:
        input_filename=os.path.join(ntu_path, skeleton_file)
        # Get the action label for the current data
        action_label = int(skeleton_file.split('A')[1][:3]) #S017C003P020R002A055.skeleton => 055
        # If the action label is in the list of actions to extract, save the data
        if action_label in subset_actions:
            output_filename = os.path.join(output_path, skeleton_file)
            shutil.copy(input_filename , output_path)



def spilt_dataset():
    path = '/Users/jeffreylu/Desktop/NTUdataset/subset' # 文件夹目录，存放所有56880个样本的文件夹
    training_path='/Users/jeffreylu/Desktop/NTUdataset/Cross-View-Train'
    test_path='/Users/jeffreylu/Desktop/NTUdataset/Cross-View-Test'

    files = os.listdir(path)    # 得到文件夹下的所有文件名称
    train = ['C002', 'C003']
    test = ['C001']
    for file in files:  # 遍历文件夹
        for i in range(2):
            if train[i] in file:
                file = os.path.join(path, file)
                if not os.path.exists(training_path):
                    os.makedirs(training_path)
                shutil.copy(file, training_path)
        for i in range(1):
            if test[i] in file:
                file = os.path.join(path,file)
                if not os.path.exists(test_path):
                    os.makedirs(test_path)
                shutil.copy(file, test_path)

getSubset_NTU(ntu_path,output_path)
spilt_dataset()
#-------------------------------------------------------------

