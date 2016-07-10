import select
import socket
import Queue
import sys
import time

addr = ('localhost', 9080)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

server.bind(addr)

server.listen(5)

###
inputs = [server]
outputs = []
message_q = {}

while inputs:
	print >> sys.stderr, "\n Waiting...."
	readable, writable, excpt = select.select(inputs, outputs, inputs)
	print readable, writable, excpt
	# time.sleep(100)

	for s in readable:
		if s is server:
			conn, client = s.accept()
			print >>sys.stderr, 'new connection from', client
			conn.setblocking(0)
			inputs.append(conn)
			message_q[conn] = Queue.Queue()
		else:
			data = s.recv(1024)
			if data:
				print >>sys.stderr, 'received "%s" from %s' % (data, s.getpeername())
				message_q[s].put(data)
				if s not in outputs:
					outputs.append(s)
			else:
				print >>sys.stderr, 'closing', client, 'after reading no data'
				if s in outputs:
					outputs.remove(s)
				inputs.remove(s)
				s.close()

				del message_q[s]

	for s in writable:
		try:
			next_msg = message_q[s].get_nowait()
		except Queue.Empty:
			print >>sys.stderr, 'output queue for', s.getpeername(), 'is empty'
			outputs.remove(s)
		else:
			print >>sys.stderr, 'sending "%s" to %s' % (next_msg, s.getpeername())
			s.send(next_msg)

	for s in excpt:
		print >>sys.stderr, 'handling exceptional condition for', s.getpeername()
		inputs.remove(s)
		if s in outputs:
			outputs.remove(s)
		s.close()

		del message_q[s]
