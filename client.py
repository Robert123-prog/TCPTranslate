import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('193.231.20.76', 5556))
s.connect(('127.0.0.1', 6666))

s.send(b"Salut frate!")
response = s.recv(1000).decode('utf-8')
print(response)
s.close()



# try:
#     s.send(b"Salut frate!")
#     response = s.recv(1000).decode('utf-8')
#     print(response)
# except Exception as e:
#     print('Connection error')
# finally:
#     s.close()