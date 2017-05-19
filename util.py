import cv2

PORT = 0
threshold = 15
WIDTH = 640
HEIGHT=480


def is_down(contour):
    global threshold
    for value in contour:
        real_value = value[0]
        if real_value[1] < threshold:
            return True
    return False


def find_position(contours):
    global WIDTH
    for contour in contours:
        if is_down(contour):
            M = cv2.moments(contour)
            x = int(M["m10"] / M["m00"])
            y = int(M["m01"] / M["m00"])
            return  (x/ WIDTH - 0.5,y/HEIGHT -0.5),contour
    return (-0.5, 0.5),None
