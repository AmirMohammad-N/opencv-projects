import cv2
import matplotlib.pyplot as plt

img = cv2.imread("E:/Desktop/New folder (5)/PNG_transparency_demonstration_2.png", cv2.IMREAD_UNCHANGED)

bgr_image = img[...,0:3]
alpha_image =  img[...,-1]

rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)
plt.title("RGB")


plt.show()


cv2.waitKey()