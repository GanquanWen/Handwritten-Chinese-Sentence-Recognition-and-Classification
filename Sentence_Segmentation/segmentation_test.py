import random
import numpy as np
import random
import os
import cv2

# len_sentence = 10
# num_sample = 1000
orig_path = 'C:/Users/Chenyu/Desktop/500_project/modify_test58'
saved_path = 'C:/Users/Chenyu/Desktop/test/'
truth_path = 'C:/Users/Chenyu/Desktop/truth/'

def generate_test(orig_path, saved_path, truth_path):
    truth_list = []
    interval_img = 255* np.ones((58,1,3))
    fp = open(truth_path + 'truth.txt','w+')
    for i in range(1000):
        sent_img = 255* np.ones((58,1,3))
        file_list = []
        truth_temp_list = []
        for j in os.listdir(orig_path):
            file_list.append(j)
        random_10 = []
        for j in range(10):
            random_10.append(file_list[random.randint(0, len(file_list)-1)])
        for j in range(10):
            truth_temp_list.append(dict_new[int(random_10[j])])
            image_path = orig_path + '/' + random_10[j]
            char_list = []
            for k in os.listdir(image_path):
                char_list.append(k)
            image = cv2.imread(image_path + '/' + char_list[random.randint(0, len(char_list)-1)])
            sent_img = np.hstack((sent_img, interval_img)) 
            sent_img = np.hstack((sent_img, image)) 
        cv2.imwrite(saved_path+str(i)+'.png', sent_img)
        truth_list.append(truth_temp_list)
    output = open(truth_path + 'truth.txt','w', encoding = "utf8")
    for row in truth_list:
        rowtxt = '{},{},{},{},{},{},{},{},{},{}'.format(row[0],row[1],row[2],row[3], row[4],row[5],row[6],row[7],row[8],row[9])
        output.write(rowtxt)
        output.write('\n')
    output.close()

generate_test(orig_path, saved_path,truth_path)