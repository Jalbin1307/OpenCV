import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ... ")
        break
    frame = cv.flip(frame, 0)

    out.write(frame)

    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()