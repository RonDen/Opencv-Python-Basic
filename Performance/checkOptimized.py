import cv2 as cv
from time import time


def testcase1(num:int):
    img = cv.imread('../imgs/messi5.jpg')
    print(cv.useOptimized())
    e1 = cv.getTickCount()
    t1 = time()
    for i in range(5, num, 2):
        # print(i)
        img = cv.medianBlur(img, i)
    e2 = cv.getTickCount()
    t2 = time()
    t = (e2 - e1) / cv.getTickFrequency()
    t_p = (t2 - t1)
    print(t)
    print(t_p)


if __name__ == '__main__':
    print(cv.useOptimized())
    testcase1(51)
    cv.setUseOptimized(False)
    print(cv.useOptimized())
    testcase1(51)
