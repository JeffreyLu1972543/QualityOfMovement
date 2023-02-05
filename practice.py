import glob
import os
import numpy as np
a="[gp]*"
os.chdir("/Users/jeffreylu/Desktop/QualityOfMovement")
for fpath in glob.glob('*.py'):
    print(len(fpath))
    # with open(fpath, 'r') as f: 
    #     print(fpath)
# a=np.arange(1,10,1)
# print(a)
# import json
# import osd
# import numpy as np
# l=[]
# with open('DSC_0808_000000000000_keypoints.json') as f :
#     a=json.load(f)
#     # print(a["people"][0]["pose_keypoints"])
#     b=a["people"][0]["pose_keypoints"]
#     c=np.array(b).reshape(-1,3)
#     d=c[:,0]
#     e=c[:,1]
#     f=np.concatenate((d,e),axis=0)
#     # print(f)
#     l.append(f)
#     l.append(f)
#     l.append(f)
#     # print(len(l)) 
#     print(l[1]) 