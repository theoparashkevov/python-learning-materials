import os
import sys
import socket
import time
from datetime import datetime

HOST = '127.0.0.1'
PORT = 6558
class Client():

	def __init__(self, host:str, port:int):
		self.__server_host = host
		self.__server_port = port

		self.socket = self.__initialize_socket()

	def __initialize_socket(self):
		print(f'[{datetime.now()}][Client] : Initializing SOCKET...')
		return_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print(f'[{datetime.now()}][Client] : Initialized successfully')

		print(f'[{datetime.now()}][Client] : Connecting to {(self.__server_host, self.__server_port)} ...')
		return_socket.connect((self.__server_host, self.__server_port))
		print(f'[{datetime.now()}][Client] : Connected successfully to {(self.__server_host, self.__server_port)}')

		return return_socket

	def send_data(self, data:str):
		print(f'[{datetime.now()}][Client] : sending data => {data}')
		self.socket.sendall(data.encode('utf-8'))
		print(f'[{datetime.now()}][Client] : data sent successfully')

	def receive_data(self, size:int):
		data = self.socket.recv(size)
		decoded_data = data.decode('utf-8')
		print(f'[{datetime.now()}][Client] : data received from the server successfully => {decoded_data}')
		return data


client = Client(HOST, PORT)
while True:
	print('---------------------------------------------')
	data_to_send = input('\n[Client]\tWhat should I send to the server ? : ')

	if data_to_send == 'terminate':
		client.send_data(data_to_send)
		client.socket.close()
		break
	else:
		client.send_data(data_to_send)
		client.receive_data(1024)