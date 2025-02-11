# Remote Procedure Call (RPC) Program - Assignment 1 (Distributed Computing)

## Description
This repository contains all the necessary dependency and main files to implement an **RPC-based arithmetic calculator**. The implementation demonstrates **client-server communication** using **gRPC** in Python.

## Prerequisites
Ensure you have **Python 3.6+** installed on your system.

## Setup Instructions
### 1. Install Dependencies
Before running the program, install the required gRPC dependencies using the following command in the **VS Code terminal**:
```sh
pip install grpcio grpcio-tools
```

### 2. Generate gRPC Code from the `.proto` File
After creating the `calculator.proto` file, run the following command in the **VS Code terminal** to generate the necessary Python files:
```sh
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
```

This will generate:
- `calculator_pb2.py` (for message serialization)
- `calculator_pb2_grpc.py` (for server-client communication stubs)

### 3. Running the Server
Start the **gRPC server** by executing:
```sh
python server.py
```

### 4. Running the Client
In a separate terminal window, execute the **gRPC client**:
```sh
python client.py
```

## Files Included
- `calculator.proto` - Protocol buffer definition for arithmetic operations.
- `server.py` - Implements the RPC server logic.
- `client.py` - Implements the RPC client logic.
- `calculator_pb2.py` - Auto-generated file for message serialization.
- `calculator_pb2_grpc.py` - Auto-generated file for gRPC service communication.

## Expected Output
1. The **server terminal** will show logs of received client requests.
2. The **client terminal** will display the results of arithmetic operations.

---
### Notes:
- Ensure the **server** is running before executing the **client**.
- Any updates to `calculator.proto` require re-running the **gRPC code generation command**.

---

This setup is specifically tested to work in **Visual Studio Code**.
