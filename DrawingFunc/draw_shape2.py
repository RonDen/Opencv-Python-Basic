import cv2 as cv
import numpy as np


if __name__ == '__main__':
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Can't open camera.")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't recive the frame (stream end?). Exiting...")
            break
        cv.rectangle(frame, (200, 0), (510, 128), (255, 255, 0), -1)
        cv.circle(frame, (250, 250), 25, (255, 0, 0), 2)
        cv.imshow("frame", frame)
        if cv.waitKey(1) == ord(' '):
            break

    cap.release()
    cv.destroyAllWindows()
