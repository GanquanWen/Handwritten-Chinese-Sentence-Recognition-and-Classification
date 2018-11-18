import numpy as np
import os
import cv2
import matplotlib.pyplot as plt

class CharSeg():
    def __init__ (self, dir_source, dir_saved, file_name, output_size = (300, 300), threshold = 2, size_flex = 0.75):
        self.dir_source = dir_source # path to the source image folder (not including the file name)
        self.dir_saved = dir_saved # path to the folder to save the segmentaion
        self.file_name = file_name
        self.output_size = output_size # The output size of each chinense character
        self.threshold = threshold # To determine if this row(or column) contains parts of the characters
        self.size_flex = size_flex # One of the parameter to the characters cutting
        self.image = cv2.imread(self.dir_source + self.file_name)
        self.image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def scan_image_horizontal(self):
        # Scan the image column by column to count how many dot in one column
        # Save all the amount in an array "horizontal"
        height = self.image_gray.shape[0]
        width = self.image_gray.shape[1]
        horizontal = np.zeros(width, dtype = int)
        for x in range(width): # From left to right
            count = 0 # The amount of dots of each column
            for y in range(height): # From top to bottom
                if (self.image_gray[y][x] < 128) :
                    count = count + 1
            horizontal[x] = count
              # print(horizontal)
        return horizontal

    def scan_image_vertical(self):
        # Scan the image row by row to count how many dot in one row
        # Save all the amount in an array "vertical"
        height = self.image_gray.shape[0]
        width = self.image_gray.shape[1]
        vertical = np.zeros(height, dtype = int)
        for y in range(height): # From top to bottom
            count = 0 # The amount of dots of each row
            for x in range(width): # From left to right
                if (self.image_gray[y][x] < 128) :
                    count = count + 1
            vertical[y] = count
        # print(vertical)
        return vertical

    def get_sentence_height(self, vertical):
        start_point = None
        end_point = None
        for i, y in enumerate(vertical):
            if y > 1 and start_point is None:
                start_point = i
            elif y > 1 and start_point is not None:
                pass
            elif y <= 1 and start_point is not None and end_point is None:
                end_point = i
            else:
                pass
        return end_point - start_point

    def segmentation(self, dots_sum, threshold, min_size):
        # Cut the sentence into characters
        # Because chinese characters are basically rectangle,
        # So we can cut it according to the height of a sentence.
        start_i = None
        end_i = None
        parts = []
        for i, val in enumerate(dots_sum):
            if val > threshold and start_i is None:
                start_i = i
            elif val > threshold and start_i is not None:
                pass
            elif val < threshold and start_i is not None:
                if i - start_i >= min_size:
                    end_i = i
                    # print(end_i - start_i)
                    parts.append((start_i, end_i))
                    start_i = None
                    end_i = None
            elif val < threshold and start_i is None:
                pass
        return parts

    def cutImage(self, img, horizontal_ranges, vertical_ranges, output_size, dir_saved):
        for y, vertical_index_pair in enumerate(vertical_ranges):
            for x, horizontal_index_pair in enumerate(horizontal_ranges):
                cutted_char = img[vertical_index_pair[0]    : vertical_index_pair[1], 
                                  horizontal_index_pair[0] : horizontal_index_pair[1]]
                resized_cutted_char = cv2.resize(cutted_char, output_size)
                cv2.imwrite(dir_saved + "row" + str(y) + "pos" + str(x) + ".jpg", resized_cutted_char)
                print("row" + str(y) + "pos" + str(x) + "saved!")

    def run(self):
        horizontal = self.scan_image_horizontal()
        vertical = self.scan_image_vertical()
        char_height = self.get_sentence_height(vertical)
        print('The height of these characters is about: ' + str(char_height) + ' pixel')
        vertical_segs = self.segmentation(vertical, self.threshold, char_height * self.size_flex)
        horizontal_segs = self.segmentation(horizontal, self.threshold, char_height * self.size_flex)
        print(vertical_segs)
        print(horizontal_segs)
        self.cutImage(self.image_gray, horizontal_segs, vertical_segs, self.output_size, self.dir_saved)










