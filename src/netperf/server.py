import time
import datetime
import socketserver


class TcpPerfHandler(socketserver.BaseRequestHandler):

    def handle(self):
        sdatetime = str(datetime.datetime.now())
        print("{} Client connect from {}".format(sdatetime, self.request.getpeername()[0]))
        total = 0
        stime = time.time()
        last_print_time = stime
        while True:
            data = self.request.recv(40960)
            if not data:
                break
            total += len(data)
            now_time = time.time()
            if now_time - last_print_time > 10:
                print("{} Got {:.2f} MB from client {} since {}, Avg speed is {:.2f} MB/s".format(
                    str(datetime.datetime.now()),
                    total/1024/1024,
                    self.request.getpeername()[0],
                    sdatetime,
                    total/1024/1024/(now_time - stime)
                ))
                last_print_time = now_time
        now_time = time.time()
        print("{} Client {} closed. It sent {:.2f} MB since {}, Avg speed is {:.2f} MB/s".format(
            str(datetime.datetime.now()),
            self.request.getpeername()[0],
            total/1024/1024,
            sdatetime,
            total/1024/1024/(now_time - stime),
        ))

def start_tcp_server(port):
    print("Netperf server start on port {}".format(port))
    with socketserver.ThreadingTCPServer(('0.0.0.0', port), TcpPerfHandler) as server:
        server.serve_forever()

def start_udp_server(port):
    pass
