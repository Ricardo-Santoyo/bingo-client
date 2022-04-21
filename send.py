import socket

HOST = socket.gethostname()
PORT = 48488

def message(message): # Sends a message to the bingo server and returns the data received by the server.
  client_socket = socket.socket()
  client_socket.connect((HOST, PORT))
  client_socket.send(message.encode())
  data = client_socket.recv(1024).decode()
  client_socket.close()

  return str(data)