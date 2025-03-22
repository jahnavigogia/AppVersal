import grpc
from django.core.management.base import BaseCommand
from users.grpc_generated import user_pb2, user_pb2_grpc


class Command(BaseCommand):
    help = "Makes a sample gRPC request to fetch user details"

    def handle(self, *args, **kwargs):
        channel = grpc.insecure_channel("localhost:50051")
        stub = user_pb2_grpc.UserServiceStub(channel)

        request = user_pb2.UserRequest(user_id=1)  # Adjust as needed
        try:
            response = stub.GetUser(request)
            self.stdout.write(f"User: {response.first_name}, Email: {response.email}")
        except grpc.RpcError as e:
            self.stderr.write(f"gRPC Error: {e.code()} - {e.details()}")
