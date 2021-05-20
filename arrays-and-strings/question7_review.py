# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

import math

def rotate(matrix):

    loop_count = math.trunc(len(matrix) / 2)
    
    for i in range(loop_count):
        for j in range(i, len(matrix) - i, 1):
            print("")


    


    return ""


matrix = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

rotate(matrix)