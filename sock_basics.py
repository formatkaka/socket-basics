import socket as s

from urlparse import urlparse as u

# Print Host Name
print s.gethostname()

# Print IP address
print s.gethostbyname('www.google.com')

# Print IP address along with Aliases
print s.gethostbyname_ex('www.google.com')

# Print host by addr
print s.gethostbyaddr('127.0.0.1') # localhost

# Get port number
p = u('http://www.google.com')
port = s.getservbyname(p.scheme)
print port

# 

def get_constants(prefix):
	return dict((getattr(s,n), n) for n in dir(s) if n.startswith(prefix))

# protocols_num =  get_constants('IPPROTO_')

# for name in ['icmp', 'udp']:
# 	pr = s.getprotobyname(name)
# 	co_name = protocols_num[pr]

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

# print families 
# print types
# print protocol

z = s.getaddrinfo('www.python.org', 'http')
print len(z)

for response in z:
	family, socktype, proto, cannon, sockaddr = response
	print 
	print 'Family        :', families[family]
	print 'Type          :', types[socktype]
	print 'Protocol      :', protocols[proto]
	print 'Canonical name:', cannon
	print 'Socket address:', sockaddr
    # print 

##### IP address respresentations #####

import binascii
import struct
import sys

str_addr = sys.argv[1]
packed_form = s.inet_aton(str_addr)

print 'Packed Form:', packed_form
print 'Original:', str_addr
print 'Packed  :', binascii.hexlify(packed_form)
print 'Unpacked:', s.inet_ntoa(packed_form)