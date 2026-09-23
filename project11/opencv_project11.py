import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("E:/Programming/a3d2bdb664a27c5c5a6b51b841e7966d.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(blur,200,300)



cv2.imshow("amir",edges)


################################################################

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5), 0)
    edges = cv2.Canny(blur, 60, 120)
    cv2.imshow('Webcam', edges)
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()