import socket
import datetime
import time
import os
from .utils import get_network_speed
from .utils import get_data_size


def run_tcp_test(server, port, total_time):
    data = os.urandom(1024*1024*8)
    data_size = len(data)
    sock = socket.socket()
    sock.connect((server, port))
    sent = 0
    counter = 0
    total_sent = 0
    sent = 0
    stime = time.clock()
    last_print_time = stime
    while True:
        sock.sendall(data)
        counter += 1
        sent += data_size
        total_sent += data_size
        now_time = time.clock()
        if now_time - last_print_time >= 5:
            print("{} {} sent to {}:{} last 5 seconds, avg speed is {}.".format(
                str(datetime.datetime.now()),
                get_data_size(sent),
                server,
                port,
                get_network_speed(sent, now_time - last_print_time),
            ))
            last_print_time = time.clock()
            sent = 0
        if now_time - stime >= total_time:
            break
    now_time = time.clock()
    print("{} {} sent to {}:{} last {} seconds, avg speed is {}.".format(
        str(datetime.datetime.now()),
        get_data_size(total_sent),
        server,
        port,
        total_time,
        get_network_speed(total_sent, now_time - stime),
    ))