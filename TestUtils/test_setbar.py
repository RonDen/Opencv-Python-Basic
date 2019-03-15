import cv2 as cv
from utils import setRGBTrackbar,\
    setBinaryTrackbar, getRGBTrackbarValue


if __name__ == '__main__':
    cv.namedWindow('image')
    setRGBTrackbar('image')
    setBinaryTrackbar('image')
    r, g, b = getRGBTrackbarValue('image')
    cv.waitKey(0)
    cv.destroyAllWindows()
