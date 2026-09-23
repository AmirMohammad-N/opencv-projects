import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("E:/Desktop/New folder (5)/unnamed.jpg",0)
cv2.imshow('orginal',image)



ret1, thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

ret2, thresh2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)

ret3, thresh3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)

ret4, thresh4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)

ret5, thresh5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)

plt.figure(figsize=(10,8))

plt.subplot(231)
plt.imshow(thresh1,cmap='gray')
plt.title("1 threshold binary")

plt.subplot(232)
plt.imshow(thresh2, cmap='gray')
plt.title("2 threshold binary inverse")

plt.subplot(233)
plt.imshow(thresh3, cmap='gray')
plt.title("3 THRESH TRUNC")

plt.subplot(234)
plt.imshow(thresh4, cmap='gray')
plt.title("4 THRESH TOZERO")

plt.subplot(235)
plt.imshow(thresh5, cmap='gray')
plt.title("5 THRESH TOZERO INV")

plt.subplot(236)
plt.imshow(image, cmap='gray')
plt.title("Orginal image")


plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
