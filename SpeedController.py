import thread
import serial
import time

sensors = {}
serial_connection = None
sending_thread = None
is_sending = False
send_queue = []
left_signal = 90
right_signal = 90


def start_refreshing(location, sending_rate=1):
    global serial_connection, is_sending, sending_thread
    if not serial_connection:
        serial_connection = serial.Serial(location, 9600)
        is_sending = True
        sending_thread = thread.start_new_thread(send_in_background, (sending_rate,))


def send_in_background(sending_rate):
    while is_sending:
        if len(send_queue):
            packet = send_queue.pop(0)
            serial_connection.write(packet)
        time.sleep(sending_rate)


def __send__(packet):
    send_queue.append(packet)
    print packet


def speed_to_signal(speed):
    x = int(round(90 * speed + 90))
    return 180 if x > 180 else 0 if x < 0 else x


def set_left(speed):
    global left_signal
    left_signal = speed_to_signal(speed)
    __send__(pack(right_signal, left_signal))


def set_right(speed):
    global right_signal
    right_signal = speed_to_signal(speed)
    __send__(pack(right_signal, left_signal))


def pack(right_sig, left_sig):
    packet = ''
    if right_sig < 100:
        packet += '0'

    if right_sig < 10:
        packet += '0'

    packet += str(right_sig)

    if left_sig < 100:
        packet += '0'

    if left_sig < 10:
        packet += '0'

    packet += str(left_sig)
    return packet
