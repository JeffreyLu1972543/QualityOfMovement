import json
import matplotlib.pyplot as plt
import numpy as np

# Define the connections between the keypoints to form the skeleton
# connections = [    [0, 1], [1, 2], [2, 3], [3, 4],  # Right arm
#     [0, 5], [5, 6], [6, 7], [7, 8],  # Left arm
#     [0, 9], [9, 10], [10, 11], [11, 12],  # Right leg
#     [0, 13], [13, 14], [14, 15], [15, 16],  # Left leg
#     [0, 17],  # Body
# ]
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
# Load the keypoints from a JSON file
with open("DSC_0808_000000000000_keypoints.json") as f:
    data = json.load(f)

# Extract the x and y coordinates of each keypoint
keypoints = np.array(data["people"][0]["pose_keypoints"]).reshape(-1, 3)[:, :2]
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
for connection in connections:
    start = keypoints[connection[0]]
    end = keypoints[connection[1]]
    ax.plot([start[0], end[0]], [start[1], end[1]], color="blue")
plt.show()