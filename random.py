import SpeedController
import time

SpeedController.start_refreshing(location='/dev/ttyACM0', sending_rate=1)

i = -1

while i < 1:
    SpeedController.set_left(i)
    SpeedController.set_right(-i)
    time.sleep(0.1)