import cv2
import numpy as np
from picamera2 import Picamera2
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

motor1_pin1 = 27
motor1_pin2 = 22
motor1_enable = 17

motor2_pin1 = 24
motor2_pin2 = 25
motor2_enable = 23

GPIO.setup(motor1_pin1, GPIO.OUT)
GPIO.setup(motor1_pin2, GPIO.OUT)
GPIO.setup(motor1_enable, GPIO.OUT)

GPIO.setup(motor2_pin1, GPIO.OUT)
GPIO.setup(motor2_pin2, GPIO.OUT)
GPIO.setup(motor2_enable, GPIO.OUT)

motor1_pwm = GPIO.PWM(motor1_enable, 100)
motor2_pwm = GPIO.PWM(motor2_enable, 100)

motor1_pwm.start(0)
motor2_pwm.start(0)

def move_forward(speed):

    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)

    GPIO.output(motor2_pin1, GPIO.HIGH)
    GPIO.output(motor2_pin2, GPIO.LOW)

    motor1_pwm.ChangeDutyCycle(speed)
    motor2_pwm.ChangeDutyCycle(speed)


def move_backward(speed):

    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.HIGH)

    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.HIGH)

    motor1_pwm.ChangeDutyCycle(speed)
    motor2_pwm.ChangeDutyCycle(speed)


def move_left(speed):

    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.LOW)

    GPIO.output(motor2_pin1, GPIO.HIGH)
    GPIO.output(motor2_pin2, GPIO.LOW)

    motor1_pwm.ChangeDutyCycle(0)
    motor2_pwm.ChangeDutyCycle(speed)


def move_right(speed):

    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)

    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.LOW)

    motor1_pwm.ChangeDutyCycle(speed)
    motor2_pwm.ChangeDutyCycle(0)


def stop_motors():

    motor1_pwm.ChangeDutyCycle(0)
    motor2_pwm.ChangeDutyCycle(0)

    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.LOW)

    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.LOW)

picam2 = Picamera2()

camera_config = picam2.create_preview_configuration(main={"size": (640, 480),"format": "RGB888"})
picam2.configure(camera_config)
picam2.start()
sleep(2)

try:

    while True:
        frame = picam2.capture_array()
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5, 5),0)
        edges = cv2.Canny(blur,60,120)

        height, width = edges.shape
        mask = np.zeros_like(edges)

        points = np.array([[(0, height),(width, height),(int(width * 0.65), int(height * 0.55)),(int(width * 0.35), int(height * 0.55))]], dtype=np.int32)

        cv2.fillPoly(mask,points,255)
        roi = cv2.bitwise_and(edges, mask)

        lines = cv2.HoughLinesP(roi,1,np.pi / 180,50,minLineLength=20,maxLineGap=40)

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
            left_line = max(left_lines,key=lambda line:(line[2] - line[0]) ** 2 +(line[3] - line[1]) ** 2)

        if len(right_lines) > 0:
            right_line = max(right_lines, key=lambda line:(line[2] - line[0]) ** 2 +(line[3] - line[1]) ** 2)

        left_x = None
        right_x = None

        if left_line is not None:
            x1, y1, x2, y2 = left_line
            cv2.line(frame,(x1, y1),(x2, y2),(0, 255, 0),3)

            if y2 != y1:
                y_bottom = heightleft_x = int(x1 +(y_bottom - y1) *(x2 - x1) / (y2 - y1))

        if right_line is not None:
            x1, y1, x2, y2 = right_line
            cv2.line(frame,(x1, y1),(x2, y2),(0, 255, 0),3)

            if y2 != y1:
                y_bottom = height
                right_x = int(x1 +(y_bottom - y1) *(x2 - x1) /(y2 - y1))

        frame_center = width // 2

        if left_x is not None and right_x is not None:

            lane_center = (left_x + right_x) // 2

            error = (lane_center -frame_center)
            cv2.line(frame,(frame_center, 0),(frame_center, height),(0, 0, 255),2)
            cv2.line(frame,(lane_center, 0),(lane_center, height),(255, 0, 0),2)

            if error < -40:
                move_left(50)
                print("LEFT", error)


            elif error > 40:
                move_right(50)
                print("RIGHT", error)
            else:
                move_forward(60)
                print("FORWARD", error)

            cv2.putText(frame,f"Error: {error}",(20, 40),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 255, 255), 2)


        else:
            stop_motors()

            cv2.putText(frame,"LANE NOT DETECTED", (20, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255),2)
            print("LANE NOT DETECTED")

        cv2.imshow("Lane Detection",frame)
        cv2.imshow("ROI",roi)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


finally:
    stop_motors()
    motor1_pwm.stop()
    motor2_pwm.stop()
    picam2.stop()
    cv2.destroyAllWindows()
    GPIO.cleanup()