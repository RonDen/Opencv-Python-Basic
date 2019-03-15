import cv2 as cv


def nothing(val):
    pass

def setRGBTrackbar(winname:str):
    cv.createTrackbar('R', winname, 0, 255, nothing)
    cv.createTrackbar('G', winname, 0, 255, nothing)
    cv.createTrackbar('B', winname, 0, 255, nothing)

def getRGBTrackbarValue(winname:str):
    r = cv.getTrackbarPos('R', winname)
    g = cv.getTrackbarPos('G', winname)
    b = cv.getTrackbarPos('B', winname)
    return r, g, b


def setBinaryTrackbar(winname:str):
    cv.createTrackbar('0 : OFF\n1 : ON', winname, 0, 1, nothing)
