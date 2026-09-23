import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ret, img = cap.read()


while True:
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    ret, img = cap.read()

    cv2.imshow('video1', hsv_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()













