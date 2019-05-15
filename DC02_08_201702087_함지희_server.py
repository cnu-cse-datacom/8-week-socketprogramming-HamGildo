import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('',9000))
data, addr= server_socket.recvfrom(2000)

print("write :", data.decode())

f = open('receive.txt', 'w')
f.write(data.decode())
f.close()
