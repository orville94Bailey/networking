import socket
import threading
import re

def threaded_recieving():
	while True:
		data = s.recv(2048)
		if not data:
			break
		if '@r username' in data:
			s.sendall(alias.encode())
			continue
		print(data.decode())

host = 'localhost'
port = 0

server = (host, 6000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

alias = raw_input('Enter your character name: ')

try:
	s.connect(server)
except socket.error as e:
	print(str(e))

print('debug message')

t = threading.Thread(target = threaded_recieving)
t.daemon = True
t.start()

while True:
	message = raw_input('-> ')
	if 'consoles are better' in message:
		s.sendall('@suicide')
		break
	s.sendall((alias + ': '+ message).encode())

s.close()
