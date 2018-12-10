import cv2
import numpy as np
import os

# make dir
os.chdir('/Users/yuchen/Desktop/Dataset/HWDB1.1')
os.mkdir('modify_test58')

# convert training set
for folder in os.listdir('/Users/yuchen/Desktop/Dataset/HWDB1.1/test'):
    if len(folder) == 5:
        os.chdir('/Users/yuchen/Desktop/Dataset/HWDB1.1/modify_test58')
        os.mkdir(folder)
        # os.chdir('/Users/yuchen/Desktop/Dataset/HWDB1.1/gray_train/' + folder)
        cwd = '/Users/yuchen/Desktop/Dataset/HWDB1.1/test/' + folder
        write_d = '/Users/yuchen/Desktop/Dataset/HWDB1.1/modify_test58/' + folder
        for r_img in os.listdir(cwd):
            if r_img != '.DS_Store':
                os.chdir(cwd)
                img = cv2.imread(r_img)
                gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                height, width = gray_img.shape
                if height > width:
                    add_1 = (height - width) // 2
                    add_2 = height - width - add_1
                    left = np.ones((add_1, height)) * 255
                    right = np.ones((add_2, height)) * 255
                    step_1 = np.insert(gray_img, 0, values=left, axis=1)
                    step_2 = np.insert(step_1, -1, values=right, axis=1)
                    new_img = cv2.resize(step_2, (58, 58), interpolation=cv2.INTER_CUBIC)
                elif height == width:
                    new_img = cv2.resize(gray_img, (58, 58), interpolation=cv2.INTER_CUBIC)
                else:
                    add_1 = (width - height) // 2
                    add_2 = width - height - add_1
                    up = np.ones((add_1, width)) * 255
                    down = np.ones((add_2, width)) * 255
                    step_1 = np.insert(gray_img, 0, values=up, axis=0)
                    step_2 = np.insert(step_1, -1, values=down, axis=0)
                    new_img = cv2.resize(step_2, (58, 58), interpolation=cv2.INTER_CUBIC)
                os.chdir(write_d)
                cv2.imwrite(r_img, new_img)
