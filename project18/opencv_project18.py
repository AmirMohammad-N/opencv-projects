import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/Pc/Desktop/New folder (2)/istockphoto-676513804-612x612.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

dst = cv2.dilate(dst,None, iterations=2)

img[dst>0.09*dst.max()]=[0,0,255]
plt.imshow(img[...,::-1])
plt.show()
