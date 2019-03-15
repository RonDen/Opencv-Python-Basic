import cv2 as cv


def opencamera(to_gray=False):
    cv.namedWindow('camera frame')
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Can't open the camera.")
        exit(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Got no frame, is it stream end? Exiting...")
            break
        if to_gray:
            frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('camera frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
