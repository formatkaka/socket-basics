import socket

import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serv_addr = ('127.0.0.1', 8080)
print >>sys.stderr, 'starting up on %s port %s' % serv_addr

sock.bind(serv_addr)

while True:
	print >>sys.stderr, '\nwaiting to receive message'
	data, addr = sock.recvfrom(4096)

	print >>sys.stderr, 'received %s bytes from %s' % (len(data), addr)
	print >>sys.stderr, data
	if data:
		sent = sock.sendto(data, addr)
		print >>sys.stderr, 'sent %s bytes back to %s' % (sent, addr)


