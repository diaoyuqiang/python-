# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import hello_bilbil_pb2 as hello__bilbil__pb2


class BilbilStub(object):
    """服务名
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HelloDyq = channel.unary_unary(
                '/test.Bilbil/HelloDyq',
                request_serializer=hello__bilbil__pb2.HelloDyqReq.SerializeToString,
                response_deserializer=hello__bilbil__pb2.HelloDyqReply.FromString,
                )
        self.HelloBoyCli = channel.unary_stream(
                '/test.Bilbil/HelloBoyCli',
                request_serializer=hello__bilbil__pb2.HelloBoyCliReq.SerializeToString,
                response_deserializer=hello__bilbil__pb2.HelloBoyCliReply.FromString,
                )
        self.HelloSend = channel.stream_unary(
                '/test.Bilbil/HelloSend',
                request_serializer=hello__bilbil__pb2.HelloSendReq.SerializeToString,
                response_deserializer=hello__bilbil__pb2.HelloSendReply.FromString,
                )
        self.TestTwoWays = channel.stream_stream(
                '/test.Bilbil/TestTwoWays',
                request_serializer=hello__bilbil__pb2.TestTwoWaysReq.SerializeToString,
                response_deserializer=hello__bilbil__pb2.TestTwoWaysResponse.FromString,
                )


class BilbilServicer(object):
    """服务名
    """

    def HelloDyq(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HelloBoyCli(self, request, context):
        """rpc HelloTest(stream HelloTestReq) returns (stream HelloTestReply){}
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HelloSend(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestTwoWays(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BilbilServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HelloDyq': grpc.unary_unary_rpc_method_handler(
                    servicer.HelloDyq,
                    request_deserializer=hello__bilbil__pb2.HelloDyqReq.FromString,
                    response_serializer=hello__bilbil__pb2.HelloDyqReply.SerializeToString,
            ),
            'HelloBoyCli': grpc.unary_stream_rpc_method_handler(
                    servicer.HelloBoyCli,
                    request_deserializer=hello__bilbil__pb2.HelloBoyCliReq.FromString,
                    response_serializer=hello__bilbil__pb2.HelloBoyCliReply.SerializeToString,
            ),
            'HelloSend': grpc.stream_unary_rpc_method_handler(
                    servicer.HelloSend,
                    request_deserializer=hello__bilbil__pb2.HelloSendReq.FromString,
                    response_serializer=hello__bilbil__pb2.HelloSendReply.SerializeToString,
            ),
            'TestTwoWays': grpc.stream_stream_rpc_method_handler(
                    servicer.TestTwoWays,
                    request_deserializer=hello__bilbil__pb2.TestTwoWaysReq.FromString,
                    response_serializer=hello__bilbil__pb2.TestTwoWaysResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'test.Bilbil', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Bilbil(object):
    """服务名
    """

    @staticmethod
    def HelloDyq(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/test.Bilbil/HelloDyq',
            hello__bilbil__pb2.HelloDyqReq.SerializeToString,
            hello__bilbil__pb2.HelloDyqReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HelloBoyCli(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/test.Bilbil/HelloBoyCli',
            hello__bilbil__pb2.HelloBoyCliReq.SerializeToString,
            hello__bilbil__pb2.HelloBoyCliReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HelloSend(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/test.Bilbil/HelloSend',
            hello__bilbil__pb2.HelloSendReq.SerializeToString,
            hello__bilbil__pb2.HelloSendReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestTwoWays(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/test.Bilbil/TestTwoWays',
            hello__bilbil__pb2.TestTwoWaysReq.SerializeToString,
            hello__bilbil__pb2.TestTwoWaysResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
