import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/Pc_Amir.Mhmd/Desktop/images.png",0)


ret, thresh = cv2.threshold(image, 127,255,0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:

    print(contour.shape)


bgr_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

cv2.polylines(bgr_image,[contours[0]],True,(0,0,255),3)
cv2.polylines(bgr_image,[contours[5]],True,(0,255,0),3)
cv2.polylines(bgr_image,[contours[4]],True,(255,0,0),3)
cv2.polylines(bgr_image,[contours[9]],True,(90,50,100),3)


plt.imshow(bgr_image[...,::-1])
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
