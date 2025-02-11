import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    # Take user input
    operation = input("Enter operation (add, subtract, multiply, divide): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    request = calculator_pb2.Operation(operation=operation, num1=num1, num2=num2)
    response = stub.Compute(request)
    
    print(f"Result: {response.result}")

if __name__ == '__main__':
    run()