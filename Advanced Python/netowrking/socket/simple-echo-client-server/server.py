import os
import sys
import socket
import time
from datetime import datetime

HOST = '127.0.0.1'
PORT = 6558
class Server():

	def __init__(self, host:str, port:int):
		self.__host = host
		self.__port = port

		self.socket = self.__initialize_socket()
		self.socket.listen()

		connection, address = self.socket.accept()
		with connection:
			print(f'[{datetime.now()}][Server] : Connected by {address}')

			while True:
				data = connection.recv(1024)
				decoded_data = data.decode('utf-8')
				print(f'[{datetime.now()}][Server] : Received data => {decoded_data}')

				if decoded_data == 'terminate':
					print(f'[{datetime.now()}][Server] : Terminating...')
					break

				connection.sendall(data)

	def __initialize_socket(self):
		print(f'[{datetime.now()}][Server] : Initializing SOCKET...')
		return_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print(f'[{datetime.now()}][Server] : Initialized successfully')

		print(f'[{datetime.now()}][Server] : Binding to {(self.__host, self.__port)} ... ')
		return_socket.bind((self.__host, self.__port))
		print(f'[{datetime.now()}][Server] : Bound successfully  to {(self.__host, self.__port)}')

		return return_socket



server = Server(HOST, PORT)