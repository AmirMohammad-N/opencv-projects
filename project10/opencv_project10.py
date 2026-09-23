import cv2
import numpy as np

cap = cv2.VideoCapture("C:/Users/Pc_Amir.Mhmd/Desktop/New folder (2)/video_2026-08-08_19-04-16.mp4")


while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100,50,50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    centers, radius = cv2.minEnclosingCircle(contours[0])
    centers = int(centers[0]), int(centers[1])
    radius = int(radius)
    cv2.circle(frame, centers, radius, (0,0,255),2)




    cv2.imshow('Object Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()



#####################################################################################

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()