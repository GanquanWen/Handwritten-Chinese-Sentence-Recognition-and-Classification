import numpy as np
import os
import cv2
import matplotlib.pyplot as plt

class CharSeg():
    # All the input images are colored(RGB)
    # if the image is already gray scale then the initialization needs to be adjusted
    def __init__ (self, dir_source, dir_saved, file_name, output_size = (300, 300), min_gray = 200, threshold = 1, min_gap = 4, rows = 1, size_flex = 0.7):
        self.dir_source = dir_source # path to the source image folder (not including the file name)
        self.dir_saved = dir_saved # path to the folder to save the segmentaion
        self.file_name = file_name
        self.output_size = output_size # The output size of each chinense character
        self.min_gray = min_gray
        self.threshold = threshold # To determine if this row(or column) contains parts of the characters
        self.min_gap = min_gap # The minimum px between two character. Means at least min_gap of blank columns(or rows) needs to be detected for the program to cut a character
        self.size_flex = size_flex # One of the parameter to the characters cutting
        self.image = cv2.imread(self.dir_source + self.file_name)
        self.image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def scan_image_horizontal(self, image, min_gray):
        # Scan the sentence column by column to count how many dot in one column
        # Save all the amount in an array "horizontal"
        height = image.shape[0]
        width = image.shape[1]
        horizontal = np.zeros(width, dtype = int)
        for x in range(width): # From left to right
            count = 0 # The amount of dots of each column
            for y in range(height): # From top to bottom
                if (image[y][x] < min_gray) :
                    count = count + 1
            horizontal[x] = count
              # print(horizontal)
        return horizontal

    def scan_image_vertical(self, image, min_gray):
        # Scan the image row by row to count how many dot in one row
        # Save all the amount in an array "vertical"
        height = image.shape[0]
        width = image.shape[1]
        vertical = np.zeros(height, dtype = int)
        for y in range(height): # From top to bottom
            count = 0 # The amount of dots of each row
            for x in range(width): # From left to right
                if (image[y][x] < min_gray) :
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
                return end_point - start_point
            else:
                pass
        if end_point is None and start_point is not None:
            end_point = len(vertical) - 1
        return end_point - start_point + 1

    def segmentation(self, dots_sum, threshold, min_size, min_gap):
        # Cut the sentence into characters
        # Because chinese characters are basically rectangle,
        # So we can cut it according to the height of a sentence.
        start_i = None
        end_i = None
        parts = []
        blank_count = 0
        for i, val in enumerate(dots_sum):
            if val > threshold and start_i is None:
                if i > 4: # Add blank around the character
                    start_i = i - 4
                else:
                    start_i = 0
            elif val > threshold and start_i is not None:
                pass
            elif val < threshold and start_i is not None:
                blank_count += 1
                if (i - start_i >= min_size) and (blank_count >= min_gap):
                    if i > len(dots_sum) - 6: # Add blank around the character
                        end_i = len(dots_sum) - 1
                    else:
                        end_i = i + 4
                    # print(end_i - start_i)
                    parts.append((start_i, end_i))
                    start_i = None
                    end_i = None
                    blank_count = 0
                else:
                    pass
            elif val < threshold and start_i is None:
                pass

        if (start_i is not None):
            end_i = len(dots_sum) - 1
            parts.append((start_i, end_i))

        return parts

    def cutImage(self, img, vertical_ranges, min_size, output_size, dir_saved):
        results = []
        for y, vertical_index_pair in enumerate(vertical_ranges):
            horizontal = self.scan_image_horizontal(img[vertical_index_pair[0] : vertical_index_pair[1], : ], self.min_gray)
            horizontal_ranges = self.segmentation(horizontal, 2, min_size, self.min_gap)
            for x, horizontal_index_pair in enumerate(horizontal_ranges):
                cutted_char = img[vertical_index_pair[0]    : vertical_index_pair[1], 
                                  horizontal_index_pair[0] : horizontal_index_pair[1]]
                resized_cutted_char = cv2.resize(cutted_char, output_size)
                results.append(resized_cutted_char)
                cv2.imwrite(dir_saved + "row" + str(y) + "pos" + str(x) + ".jpg", resized_cutted_char)
                print("row" + str(y) + "pos" + str(x) + "saved!")
        return results

    def run(self):
        vertical = self.scan_image_vertical(self.image_gray, self.min_gray)
        char_height = self.get_sentence_height(vertical)
        print('The height of these characters is about: ' + str(char_height) + ' px')
        vertical_segs = self.segmentation(vertical, self.threshold, char_height * self.size_flex, self.min_gap)
        print(vertical_segs)
        result = self.cutImage(self.image_gray, vertical_segs, char_height * self.size_flex, self.output_size, self.dir_saved)
        # print(result)
        # print(len(result))
        output = np.array(result)
        print(output)
        print(output.shape)
        print(len(output))










