import numpy as np
import os
import cv2
import math

def construct_data(path):
    y = []
    x = []
    for i in os.listdir(path):
        image_path = path + str(i)
        for j in os.listdir(image_path):
            spe_image = image_path + '/' + str(j)
            x.append(cv2.imread(spe_image))
            y.append(int(i))
    return x,y

x,y = construct_data('/Users/rzhan/Desktop/modify_test58/')
# x,y = construct_data('/Users/rzhan/Desktop/1/')


np.save('image_data.npy', x)
np.save('image_label.npy',y)


# a = np.load('image_data.npy')
# print(a.shape)