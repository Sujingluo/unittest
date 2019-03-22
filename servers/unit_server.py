import grpc
import time

from concurrent import futures

from example import data_pb2
from example import data_pb2_grpc


class Greeter(data_pb2_grpc.GreeterServicer):
    def Units2(self, request, context):
        u1 = request.text
        return data_pb2.UnitText(text=u1)

    def Units(self, request, context):
        umsg = 'unittest {msg}'
        uname = request.name
        return data_pb2.UnitReply(message='unit {msg}'.format(msg=request.name))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:8081')
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()

