import numpy as np
import matplotlib.pyplot as plt
import pickle
a=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
print(a[:,0])
b=a[:,0]
c=a[:,0].reshape((-1,2),order='F')
print(c)

connections= [  # assume it used openpose 18 keypoint model
    [0, 1], [0, 14], [0, 15],
    [1, 2], [1, 5], [1, 8],[1,11],
    [2, 3],
    [3, 4],
    [5, 6],
    [6, 7],
    [8, 9], 
    [9, 10],
    [11,12],
    [12,13],
    [14, 16],
    # [15, 17],
] 
def plot_skeleton_2(big_matrix):
    for i in range(3):# print skeletons of first 5 squats (No.0,1,2,3,4)
        single_squat=big_matrix[:,i].reshape(36,40)
        for j in range(single_squat.shape[1]):
            keypoints=single_squat[:,j].reshape((18,2),order='F')
            keypoints[:,1]=-keypoints[:,1]
            x=keypoints[10,0]
            y=keypoints[10,1]
            # keypoints[:,0]=keypoints[:,0]-x
            # keypoints[:,1]=keypoints[:,1]-y
            # Plot the skeleton
            fig, ax = plt.subplots()
            ax.set_aspect("equal")
            ax.set_xlim(-1000, 1000)
            ax.set_ylim(-1000, 1000)
            # ax.invert_yaxis()  # Flip the y-axis to match the OpenPose coordinate system)
            for k in range(keypoints.shape[0]):
                plt.scatter(keypoints[k,0], keypoints[k,1], color="red",s=4)
            for connection in connections:
                start = keypoints[connection[0]]
                end = keypoints[connection[1]]
                ax.plot([start[0], end[0]], [start[1], end[1]], color="blue")
            plt.scatter(0, 0, color="red",s=6)
            ax.text(0-250, 0-100, f'left ankle \n ({0}, {0})',fontsize=6.5)
            plt.title("No.{a} squat No.{b} frame".format(a=i,b=j))
            plt.show()


big_matrix = pickle.load(open("big_matrix.p", 'rb')) 
# select one squat to plot skeleton


plot_skeleton_2(big_matrix)
            