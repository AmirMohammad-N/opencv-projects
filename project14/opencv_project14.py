import matplotlib.pyplot as plt
import numpy as np
import cv2


original_img = cv2.imread('C:/Users/Pc/Desktop/New folder (2)/images.jfif', cv2.IMREAD_COLOR)

img = original_img.copy()

blured = cv2.GaussianBlur(original_img, (5, 5), 0)
gray = cv2.cvtColor(blured, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=20, maxLineGap=50)

lines = []
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

plt.figure(figsize=[17, 8])
plt.subplot(131);
plt.imshow(original_img[..., ::-1]);
plt.title("original Image");
plt.subplot(132);
plt.imshow(edges, cmap='gray');
plt.title("Edges");
plt.subplot(133);
plt.imshow(img, cmap='gray');
plt.title("miresult");
plt.show()