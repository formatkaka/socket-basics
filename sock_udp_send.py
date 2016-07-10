import socket

import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serv_addr = ('127.0.0.1', 8080)
# sock.bind()

try:
	# print >>sys.stderr, 'sending "%s"' % message
	send = sock.sendto(str(range(5000)), serv_addr)

	print >>sys.stderr, 'waiting to receive'
	data, serv = sock.recvfrom(16)
	print >>sys.stderr, 'received "%s"' % data

finally:
	print >>sys.stderr, 'closing socket'
	sock.close()