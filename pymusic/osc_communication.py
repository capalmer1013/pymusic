import time
from pythonosc import osc_message_builder
from pythonosc import udp_client
from pythonosc import dispatcher
from pythonosc import osc_server

class SuperColliderClient:
    def __init__(self, ip='127.0.0.1', port=57110):
        self.ip = ip
        self.port = port
        self.client = udp_client.SimpleUDPClient(self.ip, self.port)

    def send_message(self, address, *args):
        self.client.send_message(address, args)

class SuperColliderServer:
    def __init__(self, ip='127.0.0.1', port=57120):
        self.ip = ip
        self.port = port
        self.dispatcher = dispatcher.Dispatcher()
        self.server = osc_server.ThreadingOSCUDPServer((self.ip, self.port), self.dispatcher)

    def add_handler(self, address, handler):
        self.dispatcher.map(address, handler)

    def start(self):
        print(f"Serving on {self.ip}:{self.port}")
        self.server.serve_forever()

    def stop(self):
        self.server.shutdown()

if __name__ == "__main__":
    # Example usage
    sc_client = SuperColliderClient()

    def handle_message(address, *args):
        print(f"Received message at address {address}: {args}")

    sc_server = SuperColliderServer()
    sc_server.add_handler("/example", handle_message)

    try:
        sc_client.send_message("/example", "Hello, SuperCollider!")
        sc_server.start()
    except KeyboardInterrupt:
        sc_server.stop()