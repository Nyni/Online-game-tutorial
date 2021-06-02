import socket
from _thread import *
import sys

server = "10.0.0.21" #server IP
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET connects to IPv4, SOCK_STREAM defines type you use

try:
    s.bind((server,port)) #binds the server and port
except socket.error as e:
    str(e)

s.listen(2) #opens up the port, optional , if you leave it open, it lets any number connect
print("Waiting for a connection, Server Started")

def read_pos(str):
    str = str.split(",")
    return int(str[0], int(str[1]))

def make_pos(tup): #takes a tuple
    return str(tup[0]) + "," + str(tup[1])


pos = [(0,0),(100,100)]


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))

    reply = ""

    while True:
        try:
            data = read_pos(conn.recv(2048).decode()) #changes string into Tuple?
            pos[player] = data





            if not data:
                print("Disconnected")
                break

            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received: ", data)
                print("Sending: ", reply)

            conn.sendall(str.encode(make_pos(reply)))

        except:
            break

    print("Lost Connection)")
    conn.close()


currentPlayer = 0

while True: #continuous look for connections
    conn, addr = s.accept() #store connection and IP address in variables

    print("connected to: ", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
