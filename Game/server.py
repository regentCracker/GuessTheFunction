

import socket

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 8820))
server_socket.listen()
print("Server is up and running")

usernames = ['bruh']
num_of_players = int(input("num of players: "))
def get_players():
    return str(usernames)


while(len(usernames)<num_of_players):
    (client_socket, client_address) = server_socket.accept()
    print("Client connected "+str(client_address))

    username = client_socket.recv(1024).decode()
    print("Client tried to login with: " + username)
    if username not in usernames:
        client_socket.send("1".encode())
        print("succeed")
        print("players: "+get_players())
    else:
        client_socket.send("0".encode())
        print("failed")
        print("players: "+get_players())
print("starting the game")







client_socket.close()
server_socket.close()
