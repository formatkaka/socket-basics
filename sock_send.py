import socket 

import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv_addr = ('127.0.0.1', 8080)

print >>sys.stderr, 'connecting to %s port %s' % serv_addr

sock.connect(serv_addr)
print "Connected to {0}".format(serv_addr)

try:
	message = "Hello World"
	print >>sys.stderr, 'sending "%s"' % message
	sock.sendall(message)

	amt_rec = 0
	amt_expected = len(message)

	while amt_rec < amt_expected:
		data = sock.recv(16)
		amt_rec += len(data)
		print >>sys.stderr, 'received "%s"' % data
finally:
	print >> sys.stderr, 'closing socket'
	sock.close()
