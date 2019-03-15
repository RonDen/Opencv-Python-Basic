import numpy as np
import cv2 as cv


def nothing(val):
    pass

if __name__ == '__main__':
    cap = cv.VideoCapture(0)
    cv.namedWindow('image')
    cv.createTrackbar('R', 'image', 0, 255, nothing)
    cv.createTrackbar('G', 'image', 0, 255, nothing)
    cv.createTrackbar('B', 'image', 0, 255, nothing)
    if not cap.isOpened():
        print("Cannot open camera.")
        exit()
    i = 0
    while True:
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break

        r = cv.getTrackbarPos('R', 'image')
        g = cv.getTrackbarPos('G', 'image')
        b = cv.getTrackbarPos('B', 'image')

        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        frame[:, :, 0] += b
        frame[:, :, 1] += g
        frame[:, :, 2] += r
        cv.imshow('image', frame)

    cv.destroyAllWindows()
