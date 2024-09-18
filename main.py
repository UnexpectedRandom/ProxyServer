import socket
import threading
import logging


HOST = '127.0.0.1'
PORT = 8080

logging.basicConfig(filename='proxy.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Proxy:
    def __init__(self, HOST, PORT) -> None:
        self.HOST = HOST
        self.PORT = PORT
        self.server_socket = None

    def createTCP_Socket(self):

        black_listed = []


        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen(10)
        logging.info(f"Proxy server listening on {self.HOST}:{self.PORT}")
        
        while True:

            client_socket, addr = self.server_socket.accept()
            if addr[0] in black_listed:
                client_socket.close()
                logging.info(f'{addr} has been kicked due to black listed')
                return f'{addr} is black listed from the proxy'
            logging.info(f"Accepted connection from {addr}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        try:
            request = client_socket.recv(4096).decode()
            if not request:
                return

            first_line = request.split('\n')[0]
            logging.info(f"Request: {first_line}")
            
            method, url, protocol = first_line.split()
            
            if '://' in url:
                url = url.split('://')[1]
            
            host_port = url.split('/')[0]
            
            if ':' in host_port:
                target_host, target_port = host_port.split(':')
                target_port = int(target_port)
            else:
                target_host = host_port
                target_port = 80

            logging.info(f"Target host: {target_host}, Target port: {target_port}")

            target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            target_socket.connect((target_host, target_port))

            target_socket.sendall(request.encode())

            while True:
                response = target_socket.recv(4096)
                if len(response) > 0:
                    client_socket.sendall(response)
                else:
                    break

            logging.info(f"Response from {target_host} forwarded to client.")
        except Exception as e:
            logging.error(f"Error: {e}")
        finally:
            target_socket.close()
            client_socket.close()

if __name__ == "__main__":
    proxy = Proxy(HOST, PORT)
    proxy.createTCP_Socket()
