import json
import cv2
import numpy as np
 
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
    [15, 17],
] 

pose_colors = [
    (255., 0., 85.), (255., 0., 0.), (255., 85., 0.), (255., 170., 0.),
    (255., 255., 0.), (170., 255., 0.), (85., 255., 0.), (0., 255., 0.),
    (255., 0., 0.), (0., 255., 85.), (0., 255., 170.), (0., 255., 255.),
    (0., 170., 255.), (0., 85., 255.), (0., 0., 255.), (255., 0., 170.),
]

# plot skeleton from keypoint JSON file
def handle_keypoints_json(jsonfile):
    with open(jsonfile, 'r') as f:
        data = json.load(f) # load JSON

    img = cv2.imread('black.jpg') # initialize the background
 
    for d in data['people']:
        keypointMatrix = np.array(d['pose_keypoints']).reshape((18, 3)) #(x,y,c)
        for p in pose_pairs:
            pt1_list= list(map(int,keypointMatrix[p[0], 0:2])) # In order to make plot, we need to convert keypoint from float to int
            pt2_list= list(map(int,keypointMatrix[p[1], 0:2]))
            pt1 = tuple(pt1_list)
            pt2 = tuple(pt2_list)
            # when confidence is equal to 0 ...
            c1 = keypointMatrix[p[0], 2]
            c2 = keypointMatrix[p[1], 2]
            if c1 == 0.0 or c2 == 0.0:
                continue

            color = tuple(list(map(int, pose_colors[p[0]])))
            img = cv2.line(img, pt1, pt2, color, thickness=4)  # keypoints must be represented as tuple to be plotted
            img = cv2.circle(img, pt1, 6, color, thickness=-
                             1, lineType=8, shift=0)
            img = cv2.circle(img, pt2, 6, color, thickness=-
                             1, lineType=8, shift=0)

    cv2.imwrite('results/{}.jpg'.format(jsonfile), img)

handle_keypoints_json("DSC_0808_000000000000_keypoints.json")



