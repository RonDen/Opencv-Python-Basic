import numpy as np
import cv2 as cv


# Callback function, do nothing
def nothing(val):
    # it will pass the val of now trackbar pos
    print(type(val))
    print(val)
    pass


# create a black image, a window
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')

# create trackbar for color change
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF\n1: : ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

if __name__ == '__main__':
    while True:
        cv.imshow('image', img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break

        # get current positions of four trackbars
        r = cv.getTrackbarPos('R', 'image')
        g = cv.getTrackbarPos('G', 'image')
        b = cv.getTrackbarPos('B', 'image')
        s = cv.getTrackbarPos(switch, 'image')

        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]

    cv.destroyAllWindows()
