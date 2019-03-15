import cv2 as cv
import numpy as np


def nothing(val):
    pass


if __name__ == '__main__':
    cv.namedWindow('image')
    cv.createTrackbar('alpha', 'image', 0, 255, nothing)

    img1 = cv.imread("../imgs/img1.png", cv.IMREAD_UNCHANGED)
    img2 = cv.imread("../imgs/img2.png", cv.IMREAD_UNCHANGED)
    while True:
        a = 1.0 * cv.getTrackbarPos('alpha', 'image') / 255
        b = 1.0 - a
        dist = cv.addWeighted(img1, a, img2, b, 0)
        cv.imshow('image', dist)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break

    cv.destroyAllWindows()
