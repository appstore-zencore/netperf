import click
from netperf.server import start_tcp_server
from netperf.server import start_udp_server



@click.group()
def app():
    pass


@app.command()
@click.option("-p", "--port", type=int, default=5001, required=True)
@click.option("-P", "--protocol", default="tcp")
def server(port, protocol):
    if protocol.lower() == "udp":
        start_udp_server(port)
    else:
        start_tcp_server(port)


@app.command()
@click.option("-s", "--server")
@click.option("-p", "--port")
@click.option("-P", "--protocol", default="tcp")
@click.option("-t", "--time", type=int, default=0)
def client(server, port, protocol, time):
    if protocol.lower() == "udp":
        client = UdpClient(server, port)
    else:
        client = TcpClient(server, port)
    client.perf(time)


if __name__ == "__main__":
    app()
