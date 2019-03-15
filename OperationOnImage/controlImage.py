import numpy as np
import cv2 as cv


def nothing(val):
    pass


if __name__ == '__main__':
    cv.namedWindow('image')
    cv.createTrackbar('R', 'image', 0, 255, nothing)
    cv.createTrackbar('G', 'image', 0, 255, nothing)
    cv.createTrackbar('B', 'image', 0, 255, nothing)
    img = cv.imread('../basic/pkg_bot014.jpg')
    while True:
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break
        r = cv.getTrackbarPos('R', 'image')
        g = cv.getTrackbarPos('G', 'image')
        b = cv.getTrackbarPos('B', 'image')
        img[:, :, 0] += b
        img[:, :, 1] += g
        img[:, :, 2] += r
        cv.imshow('image', img)

    cv.destroyAllWindows()
