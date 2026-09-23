import cv2
import numpy as np
import matplotlib.pyplot as plt


src = cv2.imread("C:/Users/Pc/Desktop/New folder (2)/images (2).jfif")
dst = cv2.imread("C:/Users/Pc/Desktop/New folder (2)/images.jfif")


src = cv2.resize(src, None, fx=0.5, fy=0.5)
src_mask = np.zeros(src.shape, src.dtype)
poly = np.array([[22, 136],[24, 59],[113, 46],[198, 48],[241, 92],[196, 139],[22, 138]], np.int32)
cv2.fillPoly(src_mask, [poly], (255, 255, 255))

center = (180, 70)
output = cv2.seamlessClone(src,dst,src_mask,center, cv2.NORMAL_CLONE)


plt.figure(figsize=[12, 7])
plt.imshow(output[..., ::-1])
plt.axis("off")
plt.show()



###########################################################################


import cv2
import numpy as np
import matplotlib.pyplot as plt

im = cv2.imread("C:/Users/Pc/Desktop/New folder (2)/images (3).jfif")
obj = cv2.imread("C:/Users/Pc/Desktop/New folder (2)/images (4).jfif")

obj = cv2.resize(obj, None, fx=0.3, fy=0.3)
mask = 255 * np.ones(obj.shape, obj.dtype)

height, width, channels = im.shape

center = (int(width / 2), int(height / 2))

normal_clone = cv2.seamlessClone(obj, im, mask, center, cv2.NORMAL_CLONE)

mixed_clone = cv2.seamlessClone(obj, im, mask, center, cv2.MIXED_CLONE)

plt.figure(figsize=[12, 7])

plt.subplot(221)
plt.imshow(im[..., ::-1])
plt.title("image")

plt.subplot(222)
plt.imshow(obj[..., ::-1])
plt.title("obj")

plt.subplot(223)
plt.imshow(normal_clone[..., ::-1])
plt.title("normal clone")

plt.subplot(224)
plt.imshow(mixed_clone[..., ::-1])
plt.title("mixed clone")

plt.show()