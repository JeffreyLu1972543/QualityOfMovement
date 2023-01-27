import argparse
import json
import os
import cv2
import numpy as np
 
# 骨骼关键点连接对
pose_pairs = [
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

# 绘制用的颜色
pose_colors = [
    (255., 0., 85.), (255., 0., 0.), (255., 85., 0.), (255., 170., 0.),
    (255., 255., 0.), (170., 255., 0.), (85., 255., 0.), (0., 255., 0.),
    (255., 0., 0.), (0., 255., 85.), (0., 255., 170.), (0., 255., 255.),
    (0., 170., 255.), (0., 85., 255.), (0., 0., 255.), (255., 0., 170.),
]
  
def handle_json(jsonfile):
    with open(jsonfile, 'r') as f:
        data = json.load(f)

    img = cv2.imread('black.jpg')
 
    for d in data['people']:
        kpt = np.array(d['pose_keypoints']).reshape((18, 3))
        for p in pose_pairs:
            pt1 = tuple(list(map(int, kpt[p[0], 0:2])))
            c1 = kpt[p[0], 2]
            pt2 = tuple(list(map(int, kpt[p[1], 0:2])))
            c2 = kpt[p[1], 2]
            # print('== {}, {}, {}, {} =='.format(pt1, c1, pt2, c2))
            if c1 == 0.0 or c2 == 0.0:
                continue

            color = tuple(list(map(int, pose_colors[p[0]])))
            img = cv2.line(img, pt1, pt2, color, thickness=4)
            img = cv2.circle(img, pt1, 4, color, thickness=-
                             1, lineType=8, shift=0)
            img = cv2.circle(img, pt2, 4, color, thickness=-
                             1, lineType=8, shift=0)

    cv2.imwrite('results/{}.jpg'.format(jsonfile.split("\\")[-1][0:-5]), img)

handle_json("DSC_0808_000000000000_keypoints.json")
# def file_name_listdir_local(file_dir):
#     files_local = []
#     for files in os.listdir(file_dir):
#         files_local.append(files)
#     return files_local

# file_local_1 = file_name_listdir_local("./squat")
# print("file_local_1：", file_local_1[11])  # 当前目录下文件
# handle_json(./squat/file_local_1[0]")
