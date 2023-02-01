import os
import json
import numpy as np


def get_json_path(dirname):
    jsonfiles_path=[]
    for dirpath,dirnames,filenames in os.walk(dirname):
        print(len(filenames)) # get all filenames in video_detail
    for i in range(len(filenames)):
        jsonfile=os.path.join('/Users/jeffreylu/Desktop/jk_data_only_22/video_details',filenames[i]) # get path of all files in video_detail
        jsonfiles_path.append(jsonfile)
    return jsonfiles_path

def get_in_and_out(jsonfiles_path):
    in_and_outs=[]
    length=len(jsonfiles_path)
    for j in range(13):#should be for j in range(length)
        # print(j)
        with open(jsonfiles_path[j], 'r') as f:
            data = json.load(f)
            # print("hi")
            for d in data['squats']:
                in_and_outs.append(np.array(d['in_and_out']).reshape(2,-1))
    return in_and_outs

jsonfiles_path=get_json_path('/Users/jeffreylu/Desktop/jk_data_only_22/video_details')
in_and_outs=get_in_and_out(jsonfiles_path)
# print(len(in_and_outs))
openposedata_path="/Users/jeffreylu/Desktop/jk_data_only_22/openposedata"
openposedata_dirs=[name for name in os.listdir(openposedata_path) if os.path.isdir(os.path.join(openposedata_path, name))]
# print (openposedata_dirs)
inputList=[]
for i in range(len(in_and_outs)):
    Squatsforonedirectory=[]
    singleVideo=os.path.join(openposedata_path, openposedata_dirs[i])
    for dirpath,dirnames,filenames in os.walk(singleVideo):
        print(filenames)
    for j in range(in_and_outs[i].shape[0]):
        start=in_and_outs[i][j][0]
        end=in_and_outs[i][j][1]
        videoframes=np.arange(start,end,1)   
        for k in range(len(videoframes)):
            a=os.path.join(singleVideo,"DSC_0734_0000000000"+str(videoframes[k])+"_keypoints.json")
        # b=os.path.join(a,str(videoframes[k]))
        # singleframe=os.path.join(b,"_keypoints")
            with open(a, 'r') as f:
                data = json.load(f)
            for d in data['people']:
                singlesquat=(np.array(d['pose_keypoints']).reshape(-1,3))[:,1]
        Squatsforonedirectory.append(singlesquat)
        # singleSquat=np.concatenate((singleSquat,a),axis=1)
    inputList.append(Squatsforonedirectory) 
print(inputList[0])

