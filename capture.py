import image_processing
import cv2
from util import PORT, find_position, HEIGHT, WIDTH

cam = cv2.VideoCapture(PORT)
_, img = cam.read()

g = image_processing.GripPipeline()


g.process(img)
contours = g.find_contours_output
cv2.imwrite('image.png', img)
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imwrite('image_contours.png', img)
center = find_position(contours)
center = (int(center[0] * WIDTH), int(center[1] * HEIGHT))
cv2.circle(img, center, 2, (0, 255, 0), thickness=1, lineType=8, shift=0)
cv2.imwrite("image_center.png", img)

