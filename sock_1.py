import socket

import sys

# TCP/IP IPV4 socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv_addr = ('127.10.0.1', 2200)
print >>sys.stderr, 'starting up on %s port %s' % serv_addr

sock.bind(serv_addr)

sock.listen(1)

while True:
	print >> sys.stderr, 'waiting for connection'
	conn, cli_addr = sock.accept()

	try:
		print >>sys.stderr, 'connection from', cli_addr
		while True:
			data = conn.recv(16)
			print >>sys.stderr, 'received "%s"' % data
			print "My socket name : ", sock.getsockname()
			if data:
				print >>sys.stderr, 'sending data back to the client'
				conn.sendall(data)
			else:
				print >>sys.stderr, 'no more data from', cli_addr
				break
	finally:
		conn.close()
