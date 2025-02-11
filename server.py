import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Compute(self, request, context):
        if request.operation == "add":
            result = request.num1 + request.num2
        elif request.operation == "subtract":
            result = request.num1 - request.num2
        elif request.operation == "multiply":
            result = request.num1 * request.num2
        elif request.operation == "divide":
            if request.num2 == 0:
                return calculator_pb2.Result(result=float('inf'))
            result = request.num1 / request.num2
        else:
            result = 0  # Default if an invalid operation is given
        
        return calculator_pb2.Result(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()