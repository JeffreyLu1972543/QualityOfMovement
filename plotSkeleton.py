import json
import cv2
import numpy as np
import pickle
import os
pose_pairs = [  # assume it used openpose 18 keypoint model
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

pose_colors = [
    (255., 0., 85.), (255., 0., 0.), (255., 85., 0.), (255., 170., 0.),
    (255., 255., 0.), (170., 255., 0.), (85., 255., 0.), (0., 255., 0.),
    (255., 0., 0.), (0., 255., 85.), (0., 255., 170.), (0., 255., 255.),
    (0., 170., 255.), (0., 85., 255.), (0., 0., 255.), (255., 0., 170.),
]

# plot skeleton
def plot_skeleton(big_matrix ):
    for i in range(5):# print skeletons of first 5 squats (No.0,1,2,3,4)
        single_squat=big_matrix[:,i].reshape(36,40)
        for j in range(single_squat.shape[1]):
            background = cv2.imread('black.jpg') # initialize the background
            for p in pose_pairs:
                x1= int(single_squat[p[0],j])
                y1= int(single_squat[p[0]+18,j]) 
                pt1=tuple([x1,y1])
                x2= int(single_squat[p[1],j])
                y2= int(single_squat[p[1]+18,j]) 
                pt2=tuple([x2,y2])
                # when confidence is equal to 0 ...
                # c1 = keypointMatrix[p[0], 2]
                # c2 = keypointMatrix[p[1], 2]
                # if c1 == 0.0 or c2 == 0.0:
                #     continue

                color = tuple(list(map(int, pose_colors[p[0]])))
                img = cv2.line(background, pt1, pt2, color, thickness=4)  # keypoints must be represented as tuple to be plotted
                img = cv2.circle(background, pt1, 6, color, thickness=-
                                1, lineType=8, shift=0)
                img = cv2.circle(background, pt2, 6, color, thickness=-
                                1, lineType=8, shift=0)
            cv2.imwrite('/Users/jeffreylu/Desktop/skeleton_plot/No.{a}_squat{b}.png'.format(a=i,b=j), img)

# load data
squats_intepolated = pickle.load(open("squats_intepolated.p", 'rb')) 
big_matrix = pickle.load(open("big_matrix.p", 'rb')) 
# select one squat to plot skeleton
print(len(squats_intepolated))
single_squat=squats_intepolated[5]
plot_skeleton(big_matrix)






# image_folder = './results'
# video_name = 'video.avi'
# images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
# frame = cv2.imread(os.path.join(image_folder, images[0]))
# height, width, layers = frame.shape
# video = cv2.VideoWriter(video_name, 0, 1, (width,height))
# for image in images:
#     video.write(cv2.imread(os.path.join(image_folder, image)))

# cv2.destroyAllWindows()
# video.release()

