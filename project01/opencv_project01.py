import cv2
import numpy as np
import matplotlib.pyplot as plt

fig_size = (5, 5)
white_color = 255

y_crop = 20
y_crop2   = 680
x_crop = 20
x_crop2   = 680

img = cv2.imread("E:/Desktop/New folder (5)/rcnrBXzXi.jpg")

plt.figure(figsize=fig_size)
plt.title("RGB Channel")
plt.imshow(img[..., ::-1])
plt.show()

# GRAY Channel
plt.title("GRAY Channel")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img_gray, cmap='gray')
plt.show()

plt.title("W Channel")
img_white = img.copy()
img_white[y_crop:y_crop2, x_crop:x_crop2, :] = white_color
plt.imshow(img_white[..., ::-1])
plt.show()

plt.title("C Channel")
cropped = img[y_crop:y_crop2, x_crop:x_crop2]
plt.imshow(cropped[..., ::-1])
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
