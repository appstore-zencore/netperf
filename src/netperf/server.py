import time
import datetime
import socketserver


class TcpPerfHandler(socketserver.BaseRequestHandler):

    def handle(self):
        sdatetime = str(datetime.datetime.now())
        print("{} Client connect from {}".format(sdatetime, self.request.getpeername()))
        total = 0
        count = 0
        stime = time.clock()
        while True:
            size = len(self.request.recv(65536))
            if not size:
                break
            total += size
        now_time = time.clock()
        print("{} Client {} closed. It sent {:.2f} MB since {}, Avg speed is {:.2f} MB/s".format(
            str(datetime.datetime.now()),
            self.request.getpeername(),
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
