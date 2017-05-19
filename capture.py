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


cv2.drawContours(contours_img, contours, -1, (0, 0, 255), 3)
for cnt in contours:
    bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
    cv2.circle(contours_img, bottommost, 2, (0, 255, 0), thickness=1, lineType=8, shift=0)
cv2.imwrite('image_contours.png', contours_img)


center, contour = find_position(contours)
print contour
center = (int((center[0] + 0.5) * WIDTH), int((center[1]+0.5) * HEIGHT))
cv2.circle(center_img, center, 20, (0, 255, 0), thickness=1, lineType=8, shift=0)
cv2.drawContours(center_img, [contour], -1, (0, 0, 255), 3)
cv2.imwrite("image_center.png", center_img)

