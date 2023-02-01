import os
import json
import numpy as np

def flatten(l):
    return [item for sublist in l for item in sublist]
    


def get_json_path(dirname):
    jsonfiles_path=[]
    for dirpath,dirnames,filenames in os.walk(dirname):
        print(len(filenames)) # get all filenames in video_detail
    for i in range(len(filenames)):
        jsonfile=os.path.join('/Users/jeffreylu/Desktop/jk_data_only_22/video_details',filenames[i]) # get path of all files in video_detail
        jsonfiles_path.append(jsonfile)
    return jsonfiles_path

    
# length=len(jsonfiles_path)
# print(len(jsonfiles))
# print(jsonfiles)#最后要确保顺序对
def get_targetValues(jsonfiles_path):
    targetClass=[]
    for j in range(13):
        # print(j)
        with open(jsonfiles_path[j], 'r') as f:
            data = json.load(f)
            # print("hi")
            for d in data['squats']:
                targetClass.append(d['class_label'])
    targetClass_list=flatten(targetClass)   
    return targetClass_list


jsonfiles_path=get_json_path('/Users/jeffreylu/Desktop/jk_data_only_22/video_details')
targetClass_list=get_targetValues(jsonfiles_path)
print(len(targetClass_list))
print(targetClass_list)


# print(len(targetClass))
            # for d in data['squats']:
            #     squat_frames=np.array(d['in_and_out']).reshape(-1,2)
            #     print('{a}th filename, squat: {c}'.format(a=i,b=d,c=squat_frames))
         




