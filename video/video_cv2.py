import cv2 as cv
import numpy as np


if __name__ == '__main__':
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    i = 0
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        print("widht: ", cap.get(cv.CAP_PROP_FRAME_WIDTH))
        print("height: ", cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        print("frame: %i" % (i))
        i += 1
        # cap.set(cv.CAP_PROP_FRAME_HEIGHT, 320)
        # cap.set(cv.CAP_PROP_FRAME_HEIGHT, 320)
        # Display the resulting frame
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()
