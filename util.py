import cv2

PORT = 0
threshold = 15
WIDTH = 640


def is_down(contour):
    global threshold
    for value in contour:
        for i in value[:, 1]:
            if i < threshold:
                return True
    return False


def find_position(contours):
    global WIDTH
    for contour in contours:
        if is_down(contour):
            M = cv2.moments(contour)
            return int(M["m10"] / M["m00"]) / WIDTH - 0.5
    return -0.5
