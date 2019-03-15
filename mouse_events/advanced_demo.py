import cv2 as cv
import numpy as np


def nothing(val):
    pass

drawing = False  # True if mouse is pressed
mode = True  # if True, draw rectangle
ix, iy = -1, -1
r, g, b = 255, 0, 56

# mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode, r, g, b
    # print([r, g, b])
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv.rectangle(img, (ix, iy), (x, y), (b, g, r), -1)
            else:
                cv.circle(img, (x, y), 5, (b, g, r), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv.rectangle(img, (ix, iy), (x, y), (b, g, r), -1)
        else:
            cv.circle(img, (x, y), 5, (b, g, r), -1)


if __name__ == '__main__':

    cv.setMouseCallback('image', draw_circle)
    img = np.zeros((512, 512, 3), np.uint8)
    img[:] = [255, 255, 255]
    cv.namedWindow('image')
    cv.createTrackbar('R', 'image', 0, 255, nothing)
    cv.createTrackbar('B', 'image', 0, 255, nothing)
    cv.createTrackbar('G', 'image', 0, 255, nothing)

    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')

    while 1:
        cv.imshow('image', img)
        k = cv.waitKey(1) & 0xFF
        if k == ord(' '):
            mode = not mode
        elif k == 27:
            break

    cv.destroyAllWindows()
