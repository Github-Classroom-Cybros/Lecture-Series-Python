from socket import socket, gethostbyname, AF_INET, SOCK_STREAM

target = "localhost"
targetIP = gethostbyname(target)
port = 80
s = socket(AF_INET, SOCK_STREAM)

result = s.connect_ex((targetIP, port))

if(result == 0) :
 print 'Port %d is open' % (port,)
s.close()
