import cv2

PORT = 0
threshold = 15
WIDTH = 640
HEIGHT=480


def is_down(cnt):
    bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
    return bottommost[1] > HEIGHT - threshold


def find_position(contours):
    global WIDTH
    for contour in contours:
        if is_down(contour):
            M = cv2.moments(contour)
            x = int(M["m10"] / M["m00"])
            y = int(M["m01"] / M["m00"])
            return (x/WIDTH, y/HEIGHT), contour
    return (-0.5, 0), None
