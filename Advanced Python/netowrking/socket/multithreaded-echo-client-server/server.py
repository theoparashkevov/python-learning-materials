import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

class VNCServer():

    def __init__(self):
        self.socket = None
        
        self.__initialize_socket()

    def __initialize_socket(self):
        print('Initializing socket for server')
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((HOST, PORT))

    def listen(self):
        print('Listening for connections')
        self.socket.listen()

    def accept_connections(self):
        print('Accepting connections')
        counter = 0
        
        while counter < 2:
            __connection, __address =  self.socket.accept()
            socket_connection_t = threading.Thread(target=self.__create_a_connection_thread, args=(__connection, __address, ))
            socket_connection_t.start()

            counter += 1
            
        

    def __create_a_connection_thread(self, __connection, __address):
        with __connection as connection:
            print(f'Accepted connection from {__address}')
            accepting_data = True
            while accepting_data:
                data = connection.recv(1024)
                print(f'Received [{len(data)}] of data => {data.decode("utf-8")}')
                if not data:
                    accepting_data = False



# -------------------------------
# Main
# -------------------------------

if __name__ == "__main__":
    server = VNCServer()
    server.listen()
    server.accept_connections()
