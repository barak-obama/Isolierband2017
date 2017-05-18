import image_processing
import cv2
from util import PORT

cam = cv2.VideoCapture(PORT)
_, img = cam.read()

g = image_processing.GripPipeline()


g.process(img)
contours = g.find_contours_output
cv2.imwrite('image.png', img)
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imwrite('image_contours.png', img)