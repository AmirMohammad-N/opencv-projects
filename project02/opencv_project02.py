import matplotlib.pyplot as plt
import cv2

img = cv2.imread("E:/Desktop/New folder (5)/unnamed.jpg")

b,g,r = cv2.split(img)

hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hue = hsv_image[:,:,0]
saturation = hsv_image[:,:,1]
value = hsv_image[:,:,2]

plt.figure(figsize=[20,5])

plt.subplot(141)
plt.imshow(r, cmap='gray')
plt.title("Red Channel")

plt.subplot(142)
plt.imshow(g, cmap='gray')
plt.title("Green Channel")

plt.subplot(143)
plt.imshow(b, cmap='gray')
plt.title("Blue Channel")

plt.subplot(144)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("All Channels (RGB)")
plt.show()


plt.figure(figsize=[20,5])

import matplotlib.pyplot as plt
import cv2

img = cv2.imread("E:/Desktop/New folder (5)/unnamed.jpg")

b,g,r = cv2.split(img)

hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hue = hsv_image[:,:,0]
saturation = hsv_image[:,:,1]
value = hsv_image[:,:,2]

plt.figure(figsize=[10,5])

plt.subplot(141)
plt.imshow(r, cmap='gray')
plt.title("Red Channel")

plt.subplot(142)
plt.imshow(g, cmap='gray')
plt.title("Green Channel")

plt.subplot(143)
plt.imshow(b, cmap='gray')
plt.title("Blue Channel")

plt.subplot(144)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("All Channels (RGB)")
plt.show()


plt.figure(figsize=[20,5])

plt.subplot(131)
plt.imshow(hue, cmap='gray')
plt.title("Hue Channel")

plt.subplot(132)
plt.imshow(saturation, cmap='gray')
plt.title("Saturation Channel")

plt.subplot(133)
plt.imshow(value, cmap='gray')
plt.title("Value Channel")

plt.show()


plt.subplot(131)
plt.imshow(hue, cmap='gray')
plt.title("Hue Channel")

plt.subplot(132)
plt.imshow(saturation, cmap='gray')
plt.title("Saturation Channel")

plt.subplot(133)
plt.imshow(value, cmap='gray')
plt.title("Value Channel")

plt.show()
