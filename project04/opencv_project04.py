import cv2
import numpy as np
import matplotlib.pyplot as plt


image = np.zeros((512,512,3), np.uint8)
cv2.line(image, (0,0), (511,511), (255,127,0), 5)
plt.imshow(image[...,::-1])
plt.show()


image = np.zeros((512,512,3), np.uint8)
cv2.rectangle(image, (150,150), (300,250), (0,0,255), 5)
plt.imshow(image[...,::-1])
plt.show()


image = np.zeros((512,512,3), np.uint8)
cv2.circle(image, (350, 350), 100, (15,75,50), 5)
plt.imshow(image[...,::-1])
plt.show()


img = cv2.imread("E:/Desktop/New folder (5)/unnamed.jpg")
cv2.rectangle(img, (110,210), (300,340), (0,255,255), 5)
plt.imshow(img[...,::-1])
plt.show()


image = np.zeros((512,512,3), np.uint8)
cv2.putText(image, 'Hello World!', (75,290), cv2.FONT_HERSHEY_COMPLEX, 2, (100,170,0), 3)
plt.imshow(image[...,::-1])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
