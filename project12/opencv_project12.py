import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/Pc/Desktop/New folder (2)/images.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()
kp = orb.detect(img,None)

kp, des = orb.compute(img, kp)
print(des.shape)
img=cv2.drawKeypoints(img,kp,img)
plt.imshow(img)
plt.show()
#//////////////////////////////////////////////////////////////

import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('C:/Users/Pc/Desktop/New folder (2)/images.png')
img2 = cv2.imread('C:/Users/Pc/Desktop/New folder (2)/images.jfif')

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = False)

matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)
img_result = cv2.drawMatches(img1,kp1,img2,kp2,matches[:20],None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

plt.figure(figsize=[20,10])
plt.imshow(img_result[...,::-1]),plt.show();
print("\nNumber of Matching Keypoints Between The Training and Query Images: ", len(matches))