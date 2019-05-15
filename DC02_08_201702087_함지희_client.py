import socket
FLAGS = None
class ClientSocket():

	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	
	def socket_send(self):
		f = open('send.txt', 'r', encoding = 'utf8')

		self.socket.sendto(f.read(2048).encode(), (FLAGS.ip, FLAGS.port))
		print("send complete")
		f.close()


	def main(self):
		self.socket_send()

	
if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--ip', type=str, default = 'localhost')
	parser.add_argument('-p', '--port', type=int, default=8080)

	FLAGS, _= parser.parse_known_args()

	client_socket = ClientSocket()
	client_socket.main()

