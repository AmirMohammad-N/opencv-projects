import numpy as np
import cv2

cap = cv2.VideoCapture('C:/Users/Pc/Desktop/New folder (2)/slow_traffic_small.mp4')

feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

color = np.random.randint(0, 255, (100, 3))

ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

mask = np.zeros_like(old_frame)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
height, width = old_frame.shape[:2]
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        print('No frames grabbed!')
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    if p1 is None:
        break

    good_new = p1[st.flatten() == 1]
    good_old = p0[st.flatten() == 1]

    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), color[i % 100].tolist(), 2)
        frame = cv2.circle(frame, (int(a), int(b)), 5, color[i % 100].tolist(), -1)

    img = cv2.add(frame, mask)
    out.write(img)
    cv2.imshow('frame', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)

cap.release()
out.release()
cv2.destroyAllWindows()