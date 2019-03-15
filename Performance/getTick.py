import cv2 as cv
import numpy as np
from time import time


if __name__ == '__main__':
    img = cv.imread('../imgs/messi5.jpg')
    e1 = cv.getTickCount()
    t1 = time()
    for i in range(5, 51, 2):
        # print(i)
        img = cv.medianBlur(img, i)
    e2 = cv.getTickCount()
    t2 = time()
    t = (e2 - e1) / cv.getTickFrequency()
    t_p = (t2 - t1)
    print(t)
    print(t_p)
# Result I got is 0.152 seconds
# test in time
# Result I got is 0.1858(9) seconds, almost not differ
