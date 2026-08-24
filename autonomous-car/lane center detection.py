import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 60, 120)

    height, width = edges.shape
    mask = np.zeros_like(edges)

    points = np.array([[(0, height),(width, height),(int(width * 0.65), int(height * 0.55)),(int(width * 0.35), int(height * 0.55))]])

    cv2.fillPoly(mask, points, 255)
    roi = cv2.bitwise_and(edges, mask)

    lines = cv2.HoughLinesP(roi,1,np.pi / 180,50,minLineLength=20, maxLineGap=40)

    left_lines = []
    right_lines = []

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]

            if x2 == x1:
                continue
            slope = (y2 - y1) / (x2 - x1)

            if slope < -0.5:
                left_lines.append((x1, y1, x2, y2))

            elif slope > 0.5:
                right_lines.append((x1, y1, x2, y2))

    left_line = None
    right_line = None

    if len(left_lines) > 0:
        left_line = left_lines[0]

    if len(right_lines) > 0:
        right_line = right_lines[0]

    left_x = None
    right_x = None

    if left_line is not None:
        x1, y1, x2, y2 = left_line
        cv2.line(frame,(x1, y1),(x2, y2),(0, 255, 0),3)


        if y2 != y1:
            y_bottom = height
            left_x = int(x1 + (y_bottom - y1) *(x2 - x1) / (y2 - y1))


    if right_line is not None:

        x1, y1, x2, y2 = right_line
        cv2.line(frame,(x1, y1),(x2, y2),(0, 255, 0),3)

        if y2 != y1:
            y_bottom = height
            right_x = int(x1 + (y_bottom - y1) *(x2 - x1) / (y2 - y1))


    if left_x is not None and right_x is not None:
        lane_center = (left_x + right_x) // 2
        frame_center = width // 2
        error = lane_center - frame_center

        cv2.line(frame,(frame_center, 0),(frame_center, height),(0, 0, 255),2)

    cv2.imshow("Camera", frame)
    cv2.imshow("ROI", roi)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()