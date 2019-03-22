import grpc


from example import data_pb2_grpc
from example import data_pb2


def run():
    conn = grpc.insecure_channel('localhost:8081')
    client = data_pb2_grpc.GreeterStub(channel=conn)
    uu = client.Units2(data_pb2.UnitText(text='unittext success'))
    print(uu.text)

    # ut = client.Units(data_pb2.UnitReply(name='...'))
    # print(ut.message)


if __name__ == '__main__':
    run()

    