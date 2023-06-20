import socket
import time
import threading


HOST = "127.0.0.1"  
PORT = 65432        
SLEEP_TIMER = 2

class VNCClient():

    def __init__(self, client_id):
        self.socket = None
        self.__id   = client_id

        self.__initialize_socket()

    def __initialize_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.socket.connect((host, port))

    def send_data(self, data):
        self.socket.send(data)

    def send_demo_data(self):
        
        for i in range(0, 10):
            print(f'[Client_{self.__id}]', end=' ')
            data_to_be_sent_str = f'[Client_{self.__id}] Some data [{i}]'
            data_to_be_sent     = bytes(data_to_be_sent_str, encoding='utf-8')

            print(f'\tSending... "{data_to_be_sent_str}"', end=' ')
            self.send_data(data_to_be_sent)
            print(f'\t Data sent succesfully \t sleeping for {SLEEP_TIMER}s', end='\n')
            time.sleep(SLEEP_TIMER)
        



def create_client(client_id):
    client = VNCClient(client_id)
    client.connect(HOST, PORT)
    client.send_demo_data()


# -------------------------------
# Main
# -------------------------------
if __name__ == "__main__":

    client_1 = threading.Thread(target=create_client, args=(1, ))
    client_2 = threading.Thread(target=create_client, args=(2, ))

    client_1.start()
    client_2.start()


