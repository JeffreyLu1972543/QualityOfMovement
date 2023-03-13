import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle


#https://stackoverflow.com/questions/62149605/plotting-skeleton-point-in-3d-plot-using-python

NTUsubset_matrix = pickle.load(open("NTU_bigMatrix.p", 'rb'))
print(NTUsubset_matrix.shape)
# feature_matrix = np.load('feature_matrix.npy')

# Define the connections between the joints
connections = [(0, 1), (1, 2), (2, 3), (3, 4), (1, 5), (5, 6), (6, 7), (1, 8), (8, 9), (9, 10), (10, 11), (8, 12), (12, 13), (13, 14), (0, 15), (15, 17), (0, 16), (16, 18), (14, 19), (19, 20), (14, 21), (11, 22), (22, 23), (11, 24)]


def plot_skeleton_2(big_matrix):
    for i in range(3):# print skeletons of first 5 squats (No.0,1,2,3,4)
        single_squat=big_matrix[:,i].reshape(75,206)
        for j in range(single_squat.shape[1]):
            keypoints=single_squat[:,j].reshape((25,3),order='F')
            keypoints[:,1]=-keypoints[:,1]#y轴反过来
            x=keypoints[10,0]
            y=keypoints[10,1]
            z=keypoints[10,2]

            # keypoints[:,0]=keypoints[:,0]-x
            # keypoints[:,1]=keypoints[:,1]-y
            # Plot the skeleton
           

# Plot the 3D scatter

            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.set_aspect("auto")
            # ax.invert_yaxis()  # Flip the y-axis to match the OpenPose coordinate system)
            for k in range(keypoints.shape[0]):
                ax.scatter(keypoints[k,0],keypoints[k,1], keypoints[k,2],color="red",s=4)
                # plt.scatter(keypoints[k,0],keypoints[k,1], keypoints[k,2],color="red",s=4)
            for connection in connections:
                start = keypoints[connection[0]]
                end = keypoints[connection[1]]
                ax.plot([start[0], end[0]], [start[1], end[1]],[start[2], end[2]],color="blue")
                ax.plot([start[0], end[0]], [start[1], end[1]],[start[2], end[2]],color="blue")
        #         for connection in connections:
        #     joint1 = connection[0]
        # joint2 = connection[1]
        # x_values = [x[joint1], x[joint2]]
        # y_values = [y[joint1], y[joint2]]
        # z_values = [z[joint1], z[joint2]]
        # ax.plot(x_values, y_values, z_values)
            # plt.scatter(0, 0, color="red",s=6)
            # ax.text(0-250, 0-100, f'left ankle \n ({0}, {0})',fontsize=6.5)
            plt.title("No.{a} squat No.{b} frame".format(a=i,b=j))
            plt.show()

plot_skeleton_2(NTUsubset_matrix)



#-----------
# Load the keypoints data from OpenPose
# keypoints = np.load('keypoints.npy')


# num_frames = keypoints.shape[1]
# num_joints = keypoints.shape[0] // 3
# keypoints = keypoints.reshape((num_frames, num_joints, 3))

# # Plot each frame
# for i in range(num_frames):
#     # Create a new figure
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')

#     # Get the x, y, and z coordinates of the joints for the current frame
#     x = keypoints[i, :, 0]
#     y = keypoints[i, :, 1]
#     z = keypoints[i, :, 2]

#     # Plot the joints as points
#     ax.scatter(x, y, z)

#     # Plot the connections between the joints as lines
#     for connection in connections:
#         joint1 = connection[0]
#         joint2 = connection[1]
#         x_values = [x[joint1], x[joint2]]
#         y_values = [y[joint1], y[joint2]]
#         z_values = [z[joint1], z[joint2]]
#         ax.plot(x_values, y_values, z_values)

#     # Set the limits of the plot to include all the data
#     max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max() / 2.0
#     mid_x = (x.max() + x.min()) * 0.5
#     mid_y = (y.max() + y.min()) * 0.5
#     mid_z = (z.max() + z.min()) * 0.5
#     ax.set_xlim(mid_x - max_range, mid_x + max_range)
#     ax.set_ylim(mid_y - max_range, mid_y + max_range)
#     ax.set_zlim(mid_z - max_range, mid_z + max_range)

#     # Show the plot
#     plt.show()