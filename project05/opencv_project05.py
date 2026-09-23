import cv2
import numpy as np

def draw_circle(event,x,y,flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x ,y), 10, (15, 75, 50), -1)

img = np.zeros((512,512,3), np.uint8)

cv2.namedWindow("image")
cv2.setMouseCallback("image",draw_circle)

while True:
    cv2.imshow("image", img)
    if cv2.waitKey(1) == 27:
        break


#############################################################################################



draw = False
color = (255, 0, 0)
def drawing(event,x,y,flags, param):
    global draw
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw == True:
            cv2.circle(img, (x, y), 5, color, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False


img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow("image1")
cv2.setMouseCallback("image1",drawing)

while True:
    cv2.imshow("image1", img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('b'):
        color = (255,0,0)
    elif k == ord('g'):
        color = (0, 255, 0)
    elif k == ord('r'):
        color = (0, 0, 255)

    elif k == 27 & 0XFF:
        break
cv2.destroyAllWindows()











