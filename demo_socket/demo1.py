import socket


sock = socket.socket()
sock.bind(('127.0.0.1', 8081))
sock.listen(5)


while True:
    conn,addr = sock.accept()
    data = conn.recv(8096)
    conn.send(b'123123')
    conn.close()
