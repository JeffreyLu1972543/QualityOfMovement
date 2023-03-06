import os
import numpy as np
from scipy import interpolate

data_dir = "/Users/jeffreylu/Desktop/NTUdataset/Cross-View-Train" 
num_frames = 300 # intepolate each action to this number
num_keypoints = 25 # openpose 25-keypoints
num_coordinates = 3 # x,y,z

# get a list of all the files in the data directory
files = os.listdir(data_dir)

# create an empty feature matrix
num_files = len(files)
feature_matrix = np.zeros((num_frames*num_keypoints*num_coordinates, num_files))

for file in enumerate(files):
    