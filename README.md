**# ProxyServer**# Simple Python Proxy Server

This project implements a simple multithreaded TCP proxy server in Python using sockets. It logs all requests and responses, while handling basic connection forwarding between a client and target server.

## Features
- **Connection Forwarding**: Receives requests from a client and forwards them to the target server, then sends the response back to the client.
- **Multithreading**: Handles multiple client connections concurrently using Python's `threading` module.
- **Blacklist Support**: Allows blocking connections from specific IP addresses.
- **Logging**: Logs connections, requests, responses, and errors to `proxy.log`.

## Prerequisites
- Python 3.x

## How to Use

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install Dependencies**: (No external dependencies required, built with Python's standard libraries)

3. **Run the Proxy Server**:
    ```bash
    python proxy.py
    ```

   The proxy server will start listening for connections on `127.0.0.1:8080` by default. You can modify the `HOST` and `PORT` in the script if needed.

4. **Blacklist IPs**: 
   To blacklist an IP, add the IP address to the `black_listed` list inside the `createTCP_Socket` method. Blacklisted IPs will be denied access and logged in the `proxy.log` file.

## Proxy Functionality

- When a client connects to the proxy, the proxy will forward its request to the destination server, then pass the response back to the client.
- The proxy logs each connection, request, and response details in a `proxy.log` file.
  
## Code Structure

- `Proxy`: The main class that handles client connections and request forwarding.
- `createTCP_Socket`: Initializes the TCP socket and listens for incoming client connections.
- `handle_client`: Handles each client connection, forwarding requests and responses between the client and the target server.

## Logging

All logs are saved in `proxy.log` file, containing:
- Connection details (IP, Port)
- Requests and responses
- Errors and exceptions

## Example Log Entry

2023-09-17 12:34:56 - INFO - Proxy server listening on 127.0.0.1:8080 2023-09-17 12:35:10 - INFO - Accepted connection from ('127.0.0.1', 50530) 2023-09-17 12:35:10 - INFO - Request: GET http://example.com/ HTTP/1.1 2023-09-17 12:35:10 - INFO - Target host: example.com, Target port: 80 2023-09-17 12:35:11 - INFO - Response from example.com forwarded to client.



## Notes
- This proxy server currently only supports HTTP traffic and does not handle HTTPS traffic.
- This is a basic implementation meant for educational purposes and should not be used in production environments without further enhancements.

## License

This project is open source and available under the [MIT License](LICENSE).
