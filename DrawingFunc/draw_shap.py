import numpy as np
import cv2 as cv


if __name__ == '__main__':

    # Create a black image
    img = np.zeros((512, 512, 3), np.uint8)

    # Draw a diagonal blue line with thickness 5 pix
    cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    cv.rectangle(img, (200, 0), (510, 128), (0, 255, 0), 3)
    cv.circle(img, (447, 63), 63, (0, 0, 225), 2)
    cv.ellipse(img, (256, 256), (100, 50), 0, 0, 260, 255, -1)
    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10], [20, 70]], np.int32)
    # pts = pts.reshape((-1, 1, 2))
    cv.polylines(img, [pts], True, (0, 255, 255))
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, 'OpenCV', (10, 500), font, 3, (255, 255, 255), 2, cv.LINE_AA)
    cv.putText(img, 'Hello world', (20, 40), font, 2, (255, 255, 255), 2, cv.LINE_4)
    cv.imshow('image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
