import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('C:/Users/Pc_Amir.Mhmd/Desktop/photo_2026-08-14_20-15-00.jpg', 0)

kernel = np.ones((6,6), np.uint8)

opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)



plt.figure(figsize=[8,5])
plt.subplot(121);
plt.imshow(image, cmap='gray');
plt.title("Original");

plt.subplot(122);
plt.imshow(opening, cmap='gray');
plt.title("Opening");

plt.show()




image = cv2.imread('C:/Users/Pc_Amir.Mhmd/Desktop/photo_2026-08-14_20-14-55.jpg', 0)

kernel = np.ones((6,6), np.uint8)

closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

plt.figure(figsize=[8,5])
plt.subplot(121);
plt.imshow(image, cmap='gray');
plt.title("Original");
plt.subplot(122);
plt.imshow(opening, cmap='gray');
plt.title("Closing");

plt.show()