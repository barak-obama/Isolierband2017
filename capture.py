import image_processing
import cv2
from util import PORT, find_position, HEIGHT, WIDTH
import time

cam = cv2.VideoCapture(PORT)

for i in range(0, 30):
    cam.read()

_, img = cam.read()

# cv2.imwrite('image.png', img)


g = image_processing.GripPipeline()



g.process(img)

contours_img = img.copy()
center_img = img.copy()

contours = g.find_contours_output
cv2.imwrite('image.png', img)

center, contour = find_position(contours)
cv2.drawContours(contours_img, [contour], -1, (0, 255, 0), 3)
cv2.imwrite('image_contours.png', contours_img)
print contour
center = (int((center[0] + 0.5) * WIDTH), int((center[1]+0.5) * HEIGHT))
cv2.circle(center_img, center, 2, (0, 255, 0), thickness=1, lineType=8, shift=0)
cv2.imwrite("image_center.png", center_img)

