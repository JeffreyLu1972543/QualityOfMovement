import numpy as np
data = np.load('/Users/jeffreylu/Desktop/NTUdataset/video/S001C001P007R001A007.skeleton.npy',allow_pickle=True).item()
file_name=data["file_name"]
nbodys=data["nbodys"]
njoints=data["njoints"]
skel_bodyx=data["skel_body"]
rgb_bodyx=data["rgb_bodyx"]
depth_bodyx=data["depth_bodyx"]

print("file_name",file_name)
print("nbodys",nbodys)
print("njoints",njoints)