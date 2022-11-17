import socket

print("Welcome to Guess the Function game")
print("Rules:")
print("Every player creates a text file with a python function (20 characters and 20ms runtime limit).")
print("Your goal is to guess other people's function.")
print("For that you can send a number to the server and a player's name.")
print("The server will output only to you the result.")
print("Every turn you can guess only 1 person's function so play smart!")
print("Good luck and have fun!")
print()
print("Enter ip address:")
address = str(input())


s = socket.socket()
s.connect((address, 8820))

s.send("echo ".encode())
#check delay later
data = s.recv(1024).decode()
print(data)

s.close()
