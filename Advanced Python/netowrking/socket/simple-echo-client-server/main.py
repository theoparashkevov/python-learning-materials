from client import Client
from server import Server
import threading

HOST = '127.0.0.1'
PORT = 6558

server = Server(HOST, PORT)