import numpy as np
import cv2 as cv
from random import randint, choice

def how_many_event():
    events = [i for i in dir(cv) if 'EVENT' in i]
    print(events)


# mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
    # if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)


def random_color_draw(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 100, (randint(0, 255), randint(0, 255), randint(0, 255)), -1)
    if event == cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img, (x-30, y-30), (x+30, y+30), color=(randint(0, 255), randint(0, 255), randint(0, 255)), thickness=-1)


def draw_rectangle(event, x, y, flags, param):
    if event == cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img, (x-10, y-10), (x+10, y+10), color=(randint(0, 255), randint(0, 255), randint(0, 255)))


if __name__ == '__main__':
    # Create a black image, a window and bind the function to window
    img = np.zeros((512, 512, 3), np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image', random_color_draw)

    while(1):
        cv.imshow('image', img)
        if cv.waitKey(1) == ord(' '):
            break

    cv.destroyAllWindows()
