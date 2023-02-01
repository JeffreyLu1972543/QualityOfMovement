from audioop import add
import json
from tracemalloc import start
import cv2
import numpy as np

def handle_videoDetail_json(jsonfile):
    with open(jsonfile, 'r') as f:
        data = json.load(f)
    for d in data['squats']:
        squat_frames=np.array(d['in_and_out']).reshape(-1,2)
        print(squat_frames)
    for i in range(squat_frames.shape[0]):
       
        start=squat_frames[i][0]
        end=squat_frames[i][1]+1
        videoframes=np.arange(start,end,1)
        #print(videoframes)
    # feature_Marix=np.array([])
    # for j in videoframes:

    #     with open("?????????", 'r') as f:#？？？？？？how to construct filename 
    #         data = json.load(f)
    #     for d in data['squats']:
    #         keypointMatrix = np.array(d['pose_keypoints']).reshape((18, 3)) #(x,y,c)  
    #         feature_Marix=np.concatenate((feature_Marix, keypointMatrix ), axis = 0)
    # print(feature_Marix)
    # return feature_Marix
handle_videoDetail_json("ax.json")