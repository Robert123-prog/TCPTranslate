import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('193.231.20.76', 5556))
s.connect(('127.0.0.1', 6969))

s.send(b"Salut frate!")
print(s.recv(1000))
s.close()
