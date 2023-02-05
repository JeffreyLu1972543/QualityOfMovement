import os
import json
from this import d
import numpy as np
import glob
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
    squats_matrix=[]
    assert len(filenames)==len(in_and_outs), "Error"
    for i in range(len(filenames)):
        path=os.path.join(root_openpose_data, os.path.splitext(filenames[i])[0])
        os.chdir(path)
        cwd=os.getcwd()
        # print(cwd)
        for j in range(in_and_outs[i].shape[0]):
            frames=np.arange(in_and_outs[i][j][0],in_and_outs[i][j][1]+1,1)
            # print(frames)
            for k in range(len(frames)):
                h=in_and_outs[i][j][1]+1-in_and_outs[i][j][0]
                onesquat=np.empty(18,2*h) #18*2k
                # singleframe=str(frames[k])+".json"
                for fpath in glob.glob("*{a}*".format(a=frames[k])):#!!!!!!!!!!!!!!!!!!!!!!!!!!
                    with open(fpath, 'r') as f:
                        # print("hi")
                        data = json.load(f)
                    for d in data['people']:
                        singleframe=(np.array(d['pose_keypoints']).reshape(-1,3))[:,1]
                        onesquat=np.append((onesquat,singleframe),axis=1)
            squats_matrix.append(onesquat)
    return squats_matrix


def get_input_structure(squats_list):
    print("Length of the array is {} , which reprensents total number of squat instance")
    for i in range(len(squats_list)):
        print(squats_list[i].shape)



root_vid_details = '/Users/jeffreylu/Desktop/jk_data_only_22/video_details'
root_openpose_data ="/Users/jeffreylu/Desktop/jk_data_only_22/openposedata"
jsonfiles_path,filenames=get_json_path('/Users/jeffreylu/Desktop/jk_data_only_22/video_details')
in_and_outs=get_in_and_out(jsonfiles_path)
squats_list=get_squats(root_openpose_data,in_and_outs,filenames)
print("-----------------------------------------")
print(len(squats_list))
get_input_structure(squats_list)

# print(in_and_outs[2])
# print(jsonfiles_path)
openposedata_path="/Users/jeffreylu/Desktop/jk_data_only_22/openposedata"
openposedata_dirs=[name for name in os.listdir(openposedata_path) if os.path.isdir(os.path.join(openposedata_path, name))]
# print (openposedata_dirs)



























# inputList=[]
# for i in range(len(in_and_outs)):
#     Squatsforonedirectory=[]
#     singleVideo=os.path.join(openposedata_path, openposedata_dirs[i])
#     for dirpath,dirnames,filenames in os.walk(singleVideo):
#         #  print(filenames)
#          print("hi")
#     for j in range(in_and_outs[i].shape[0]):
#         start=in_and_outs[i][j][0]
#         end=in_and_outs[i][j][1]
#         videoframes=np.arange(start,end,1)   
#         for k in range(len(videoframes)):
#             a=os.path.join(singleVideo,"DSC_0734_0000000000"+str(videoframes[k])+"_keypoints.json")
#         # b=os.path.join(a,str(videoframes[k]))
#         # singleframe=os.path.join(b,"_keypoints")
#             with open(a, 'r') as f:
#                 data = json.load(f)
#             for d in data['people']:
#                 singlesquat=(np.array(d['pose_keypoints']).reshape(-1,3))[:,1]
#         Squatsforonedirectory.append(singlesquat)
#         # singleSquat=np.concatenate((singleSquat,a),axis=1)
#     inputList.append(Squatsforonedirectory) 
# # print(inputList[0])

