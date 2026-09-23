import RPi.GPIO as GPIO

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