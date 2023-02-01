import os
import json
import numpy as np

# root_vid_details = '/Users/jeffreylu/Desktop/jk_data_only_22/video_details'
root_vid_details = 'F:/WORK/DATASETS/jk_data_only_22/video_details'

def flatten(l):
    return [item for sublist in l for item in sublist]
# return a list of file path of all json files in video_detail folder
def get_json_path(dirname):

    jsonfiles_path=[]
    for dirpath,dirnames,filenames in os.walk(dirname):
        print(len(filenames)) # get all filenames in video_detail
    for i in range(len(filenames)):
        jsonfile=os.path.join(root_vid_details, filenames[i]) # get path of all files in video_detail
        jsonfiles_path.append(jsonfile)
    return jsonfiles_path

def get_targetValues(jsonfiles_path):
    targetClass=[]
    length=len(jsonfiles_path)
    for j in range(length):#should be for j in range(length)
        print(jsonfiles_path[j])
        with open(jsonfiles_path[j], 'r') as f:
            data = json.load(f)
            # print("hi")
            for d in data['squats']:
                targetClass.append(d['class_label'])
    targetClass_list=flatten(targetClass)   
    return targetClass_list


jsonfiles_path=get_json_path(root_vid_details)
targetClass_list=get_targetValues(jsonfiles_path)
print(len(targetClass_list))
print(targetClass_list)
         




