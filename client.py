import socket
import json

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 8889

# connect to the server on local computer
s.connect(('0.0.0.0', port))
sessionid = 'kosong'

# receive data from the server
while True:
    input = raw_input("You: ")
    s.send(str.encode("\n".join([str(sessionid), str(input)])))
    data = s.recv(1024)
    print data

    if input[:6] == 'logout':
        sessionid = 'kosong'
    elif input[:4] == 'auth':
        data = json.loads(data)
        try:
            sessionid = data['tokenid'].strip()
        except KeyError:
            pass

# close the connection
s.close()
