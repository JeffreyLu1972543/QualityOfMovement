import os
import json
import numpy as np
import pickle

root_vid_details = '/Users/jeffreylu/Desktop/jk_data_only_22/video_details'
# root_vid_details = 'F:/WORK/DATASETS/jk_data_only_22/video_details'
# A = np.zeros((18, 5))
#b = str(7)
#b.zfill(10)
#Out[22]: '0000000007'
def flatten(l):
    return [item for sublist in l for item in sublist]
# return a list of file path of all json files in video_detail folder
def get_json_path(dirname):
    jsonfiles_path=[]
    for dirpath,dirnames,filenames in os.walk(dirname):
        print("There are {len} JSON files in current directory".format(len=len(filenames))) # get all filenames in video_detail
    for i in range(len(filenames)):
        jsonfile=os.path.join(root_vid_details, filenames[i]) # get path of all files in video_detail
        jsonfiles_path.append(jsonfile)
    return jsonfiles_path

def get_class_labels(jsonfiles_path):
    class_labels_list=[]
    length=len(jsonfiles_path)
    for j in range(length):
        # print(jsonfiles_path[j])
        with open(jsonfiles_path[j], 'r') as f:
            data = json.load(f)
            for d in data['squats']:
                class_labels_list.append(d['class_label'])
    targetClass_list=flatten(class_labels_list)   
    return class_labels_list

path=get_json_path(root_vid_details)
labels=get_class_labels(path)
#results
print("-------------------------------------------------")
labels_flattenList=flatten(labels) 
print(len(labels_flattenList))
# print(labels_flattenList)
print("-------------------------------------------------")
# print(path)
# print(path)#t j07 a l j06 s02 r ry j01
# print(labels[2])
# print(labels[0])
         

fw=open('labels.p', 'wb')
pickle.dump(labels_flattenList, fw) 
fw.close()
fr=open('labels.p', 'rb')
labels_depickled = pickle.load(open('labels.p', 'rb')) 
print("Depickled label data : {a}".format(a=len(labels_depickled)))
fr.close()


