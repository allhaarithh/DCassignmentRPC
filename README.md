# DCassignmentRPC
Contains all the dependency and main files of the RPC Question(Q2) of Assignment 1 - Distributed Computing 

This works in vscode only if we type in the below code in the VSCterminal at first:
//
pip install grpcio grpcio-tools
//

Again after creating the .proto file, run the below code in the VSCode terminal:
//
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
//
