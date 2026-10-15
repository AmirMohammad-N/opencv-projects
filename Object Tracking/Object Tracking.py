import cv2

video_input_file_name = "C:/Users/Pc/Desktop/New folder (2)/slow_traffic_small.mp4"

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'CSRT', 'TLD', 'MEDIANFLOW', 'MOSSE']
tracker_type = 'CSRT'

video = cv2.VideoCapture(video_input_file_name)

if not video.isOpened():
    print("Could not open video")
    exit()

ok, frame = video.read()

if not ok:
    print("Could not read video")
    video.release()
    exit()

if tracker_type == 'BOOSTING':
    tracker = cv2.legacy.TrackerBoosting_create()
elif tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create()
elif tracker_type == 'KCF':
    tracker = cv2.TrackerKCF_create()
elif tracker_type == 'CSRT':
    tracker = cv2.TrackerCSRT_create()
elif tracker_type == 'TLD':
    tracker = cv2.legacy.TrackerTLD_create()
elif tracker_type == 'MEDIANFLOW':
    tracker = cv2.legacy.TrackerMedianFlow_create()
else:
    tracker = cv2.legacy.TrackerMOSSE_create()

bbox = cv2.selectROI("Select Object", frame, False)
cv2.destroyWindow("Select Object")

if bbox[2] == 0 or bbox[3] == 0:
    video.release()
    exit()

tracker.init(frame, bbox)

height, width = frame.shape[:2]
fps = video.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 30

video_out = cv2.VideoWriter("tracking_output.mp4",cv2.VideoWriter_fourcc(*'mp4v'),fps,(width, height))

while True:
    ok, frame = video.read()

    if not ok:
        break

    tm = cv2.TickMeter()
    tm.start()
    ok, bbox = tracker.update(frame)
    tm.stop()

    if ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2)
    else:
        cv2.putText(frame, "Tracking failure detected", (80, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.putText(frame, tracker_type + " Tracker", (80, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 170, 50), 2)
    cv2.putText(frame, "FPS: " + str(round(tm.getFPS(), 2)), (80, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 170, 50), 2)

    cv2.imshow("Object Tracking", frame)
    video_out.write(frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

video.release()
video_out.release()
cv2.destroyAllWindows()

