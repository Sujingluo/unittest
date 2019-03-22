# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from example import data_pb2 as data__pb2


class GreeterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Units = channel.unary_unary(
        '/example.Greeter/Units',
        request_serializer=data__pb2.UnitRequest.SerializeToString,
        response_deserializer=data__pb2.UnitReply.FromString,
        )
    self.Units2 = channel.unary_unary(
        '/example.Greeter/Units2',
        request_serializer=data__pb2.UnitText.SerializeToString,
        response_deserializer=data__pb2.UnitText.FromString,
        )


class GreeterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Units(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Units2(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Units': grpc.unary_unary_rpc_method_handler(
          servicer.Units,
          request_deserializer=data__pb2.UnitRequest.FromString,
          response_serializer=data__pb2.UnitReply.SerializeToString,
      ),
      'Units2': grpc.unary_unary_rpc_method_handler(
          servicer.Units2,
          request_deserializer=data__pb2.UnitText.FromString,
          response_serializer=data__pb2.UnitText.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'example.Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
