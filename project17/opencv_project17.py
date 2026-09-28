import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('C:/Users/Pc/Desktop/New folder (2)/a3d2bdb664a27c5c5a6b51b841e7966d.jpg')
height, width, _ = image.shape

T = np.float32([[1, 0, 100], [0, 1,30]])
img_translation = cv2.warpAffine(image, T, (width+100, height+30))
plt.imshow(img_translation[...,::-1])
plt.show()
print (T)

######################################################

import cv2
import numpy as np
import matplotlib.pyplot as plt

rotation_amount_degree = 10
theta = rotation_amount_degree * np.pi / 180.0

image = cv2.imread('C:/Users/Pc/Desktop/New folder (2)/a3d2bdb664a27c5c5a6b51b841e7966d.jpg')
height, width, _ = image.shape

T = np.float32([[np.cos(theta), -np.sin(theta), 50], [np.sin(theta), np.cos(theta),-50]])
img_translation = cv2.warpAffine(image, T, (width, height))
plt.imshow(img_translation[...,::-1])
plt.show()

######################################################
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/Pc/Desktop/New folder (2)/a3d2bdb664a27c5c5a6b51b841e7966d.jpg')

transposed = cv2.transpose(img)

plt.subplot(121),plt.imshow(image[...,::-1]),plt.title('Input')
plt.subplot(122),plt.imshow(transposed[...,::-1]),plt.title('Output')
plt.show()

######################################################

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/Pc/Desktop/New folder (2)/a3d2bdb664a27c5c5a6b51b841e7966d.jpg')

flipped = cv2.flip(image, 0)

plt.subplot(121),plt.imshow(image[...,::-1]),plt.title('Input')
plt.subplot(122),plt.imshow(flipped[...,::-1]),plt.title('Output')
plt.show()