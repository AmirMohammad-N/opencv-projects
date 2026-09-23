import cv2
import numpy as np
import matplotlib.pyplot as plt


src = cv2.imread("C:/Users/Pc/Desktop/New folder (2)/photo_2026-09-23_15-14-36.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

rows = gray.shape[0]
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,param1=100, param2=30,minRadius=50, maxRadius=100)


if circles is not None:
    circles = np.uint16(np.around(circles))
    for c in circles[0, :]:
        center_x,center_y, radius = c
        center = (center_x,center_y)
        cv2.circle(src, center, 1, (0, 100, 100), 3)
        cv2.circle(src, center, radius, (255, 0, 255), 3)
plt.imshow(src[...,::-1])
print("Number of coins:",len(circles[0,:]))
plt.show()