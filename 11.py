# dump() 与 load() 相比 dumps() 和 loads() 还有另一种能力：dump()函数能一个接着一个地将几个对象序列化存储到同一个文件中，随后调用load()来以同样的顺序反序列化读出这些对象。
# sion
#pickle.dump(all_meta_data, open('all_meta_data.p', 'wb')) 
#pickle.dump(all_squat_data, open('all_squat_data.p', 'wb')) 
#all_squat_data_depickled = pickle.load(open('all_squat_data.p', 'rb')) 
#all_meta_data_depickled = pickle.load(open('all_meta_data.p', 'rb')) 

#coding:utf-8
__author__ = 'MsLili'
#pickle模块主要函数的应用举例
import pickle
dataList = [[1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']]
dataDic = { 0: [1, 2, 3, 4],
            1: ('a', 'b'),
            2: {'c':'yes','d':'no'}}
 
#使用dump()将数据序列化到文件中
fw = open('dataFile.txt','wb')
# Pickle the list using the highest protocol available.
pickle.dump(dataList, fw, -1)
# Pickle dictionary using protocol 0.
pickle.dump(dataDic, fw)
fw.close()
 #使用load()将数据从文件中序列化读出
fr = open('dataFile.txt','rb')
data1 = pickle.load(fr)
print(data1)
data2 = pickle.load(fr)
print(data2)
fr.close()

import numpy as np
t=np.r_[0:5]
print(t)