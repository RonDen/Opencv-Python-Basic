import cv2 as cv
import numpy as np


# basic add
if __name__ == '__main__':
    x = np.uint8([250])
    y = np.uint8([10])
    print(cv.add(x, y))  # 255 because 250 + 10 >= 255
    print(x + y)         # 5 because 260 % 255 = 5
