import pickle
import numpy as np

squats_list = pickle.load(open("squats_original.p", 'rb')) 
print(len(squats_list))
print(squats_list[0].shape)
print(squats_list[1].shape)
print(squats_list[2].shape)