import socket
import threading

host = ''
port = 6000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = []
try:
	s.bind((host,port))
except socket.error as e:
	print(str(e))
print('Waiting for connection')
s.listen(5)

encounter_list = []

#promts second user for battle permissions
def encounder(player_1, player_2):
	player_2[0].send('Will you battle ' + player_1[1] + '?')
	while True:
		data = conn.recv(2048)

#function to run on threads
def threaded_client(conn):
	conn.send(str.encode('Welcome to the Battleground\n'))

	while True:
		data = conn.recv(2048)

		if not data:
			break
		#do something with data
		if '@suicide' in data:
			kill_client(conn)
			continue
		if '@encounter' in data:
			
		if data.decode() != '\n':
			send_to_clients(data.encode())
	conn.close()

#server thread to send messages to clients
def server_messages():
	message = raw_input('-> ')
	send_to_clients('DM: '+ message)

#send a message to all clients in list
def send_to_clients(data):
	for conn in [x[0] for x in clients]:
		conn.sendall(data)
		

#recieved dying command from client
#function removes client from connected list
def kill_client(conn):
	if conn in clients[0]:
		#this pulls the ips from the connections list
		#makes a new list containing them then
		#I search the list to find the index that needs deleted
		del clients[[x[0] for x in clients].index(conn)]
		print(clients)


#main server loop

while True:
	conn, addr = s.accept()
	if conn not in clients:
		conn.sendall('@r username')
		alias = conn.recv(1024)
		clients.append((conn,alias))
	print ('connected to: '+addr[0]+':'+str(addr[1])+' as '+ alias)

	t = threading.Thread(target = threaded_client,args =  (conn,))
	t.daemon = True
	t.start()
