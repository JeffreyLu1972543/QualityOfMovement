import os
import json
import numpy as np
import glob
import pickle

def get_json_path(root_vid_details):
    jsonfiles_path=[]
    for dirpath,dirnames,filenames in os.walk(root_vid_details):
        print("There are {len} JSON files in current directory".format(len=len(filenames))) # get all filenames in video_detail # get all filenames in video_detail
    for i in range(len(filenames)):
        jsonfile=os.path.join(root_vid_details,filenames[i]) # get path of all files in video_detail
        jsonfiles_path.append(jsonfile)
    return jsonfiles_path,filenames

def get_in_and_out(jsonfiles_path):
    in_and_outs=[]
    length=len(jsonfiles_path)
    for j in range(length):#should be for j in range(length)
        # print(j)
        with open(jsonfiles_path[j], 'r') as f:
            data = json.load(f)
            for d in data['squats']:
                in_and_outs.append(np.array(d['in_and_out']).reshape(-1,2))
    return in_and_outs

def get_squats(root_openpose_data,in_and_outs,filenames):
    squats_list=[]  # list to store all squat instance
    assert len(filenames)==len(in_and_outs), "Error"
    b=[]
    for i in range(len(filenames)):
        path=os.path.join(root_openpose_data, os.path.splitext(filenames[i])[0]) # splitext returns a tuple that represents root and ext part of the specified path name.
        os.chdir(path)
        b.append(in_and_outs[i].shape[0])
        # cwd=os.getcwd()
        # print(cwd)
        for j in range(in_and_outs[i].shape[0]):
            frames=np.arange(in_and_outs[i][j][0],in_and_outs[i][j][1]+1,1) # get all frame indexes corresponds to a single squat
            onesquat=np.zeros((36,1))
            for k in range(len(frames)):
                for fpath in glob.glob("*00000000{a}_keypoints.json".format(a=frames[k])):# variable in regular expression
                    with open(fpath, 'r') as f:
                        # print("hi")
                        data = json.load(f)
                    for d in data['people']:
                        x=(np.array(d['pose_keypoints']).reshape(-1,3))[:,0]
                        y=(np.array(d['pose_keypoints']).reshape(-1,3))[:,1]
                        singleframe=np.concatenate((x,y),axis=0).reshape(36,1)
                        # if singleframe.shape[0]!=36:
                        #   print("wrong")
                    onesquat=np.concatenate((onesquat,singleframe),axis=1)
            squats_list.append(onesquat[:,1:])
    print("The number of squats contained in each JSON file in video_detail folder :\n",b)
    return squats_list


def get_input_structure(squats_list):
    print("Length of the list is {a} , which reprensents total number of squat instance".format(a=len(squats_list)))
    for i in range(len(squats_list)):
        print("No.{a} squat is represented as an array of shape:".format(a=i),squats_list[i].shape)
    print("\nAll of these squats above form a list\n")


root_vid_details = '/Users/jeffreylu/Desktop/jk_data_only_22/video_details'
root_openpose_data ="/Users/jeffreylu/Desktop/jk_data_only_22/openposedata"
jsonfiles_path,filenames=get_json_path('/Users/jeffreylu/Desktop/jk_data_only_22/video_details')
in_and_outs=get_in_and_out(jsonfiles_path)
squats_list=get_squats(root_openpose_data,in_and_outs,filenames)
print("-----------------------------------------")
get_input_structure(squats_list)

os.chdir("/Users/jeffreylu/Desktop/QualityOfMovement")

fw=open('s.p', 'wb')
pickle.dump(squats_list, fw) 
# fw.close()
fr=open('s.p', 'rb')
all_squat_data_depickled = pickle.load(open('s.p', 'rb')) 
print(len(all_squat_data_depickled),all_squat_data_depickled[0].shape)
# fr.close()






# # print(in_and_outs[2])
# # print(jsonfiles_path)
# openposedata_path="/Users/jeffreylu/Desktop/jk_data_only_22/openposedata"
# openposedata_dirs=[name for name in os.listdir(openposedata_path) if os.path.isdir(os.path.join(openposedata_path, name))]
# # print (openposedata_dirs)

















