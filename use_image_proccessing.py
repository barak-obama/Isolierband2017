from time import sleep

import isolirband
from isolirband import *
import SpeedController
from threading import Thread

MAX_SPEED = 0.7
KP = 1.2


def tank_drive(speed_left, speed_right):
    SpeedController.set_left(speed_left)
    SpeedController.set_right(-speed_right)


def speed_by_center(center):
    global MAX_SPEED
    global KP
    if center < 0:
        tank_drive(-center * KP, MAX_SPEED)
    elif center > 0:
        tank_drive(MAX_SPEED, center * KP)
    else:
        tank_drive(MAX_SPEED, MAX_SPEED)
    return True


def loop():
    pipeline = GripPipeline()
    cam = cv2.VideoCapture(isolirband.PORT)
    while 1:
        img = cam.read()[1]
        pipeline.process(img)
        contours = pipeline.find_contours_output
        center = find_position(contours)
        print center
        speed_by_center(center)
        sleep(0.01)


if __name__ == '__main__':
    SpeedController.start_refreshing(location='/dev/ttyACM0', sending_rate=0.01)
    loop()
