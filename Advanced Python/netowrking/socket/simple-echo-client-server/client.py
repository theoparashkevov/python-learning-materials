import os
import sys
import socket
import time

HOST = '127.0.0.1'
PORT = 6558
class Client():

	def __init__(self, host:str, port:int):
		self.__server_host = host
		self.__server_port = port

		self.socket = self.__initialize_socket()

	def __initialize_socket(self):
		return_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		return_socket.connect((self.__server_host, self.__server_port))

		return return_socket

	def send_data(self, data:str):
		self.socket.sendall(data.encode('utf-8'))

	def receive_data(self, size:int):
		data = self.socket.recv(size)
		print(f"Received: {data.decode('utf-8')}")
		return data


client = Client(HOST, PORT)
while True:
	data_to_send = input('What should I send to the server ? ')

	if data_to_send == 'terminate':
		client.send_data(data_to_send)
		client.socket.close()
		break
	else:
		client.send_data(data_to_send)
		client.receive_data(1024)