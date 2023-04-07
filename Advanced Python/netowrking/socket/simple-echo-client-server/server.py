import os
import sys
import socket
import time

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
			print(f"Connected by {address}")

			while True:
				data = connection.recv(1024)
				decoded_data = data.decode('utf-8')
				print(f"Received: {decoded_data}")

				if decoded_data == 'terminate':
					print('Terminating...')
					break

				connection.sendall(data)

	def __initialize_socket(self):
		print('Initializing socket...')
		return_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


		return_socket.bind((self.__host, self.__port))
		print(f'Socket successfully bound to {self.__host}:{self.__port}')

		return return_socket



server = Server(HOST, PORT)