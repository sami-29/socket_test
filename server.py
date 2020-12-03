#importing modules
import socket
from _thread import *
from player import Player
import pickle
import sys

server = "192.168.1.35"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try :
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("waiting for a connection, server started")


players = [Player(0,0,50,50,(255,0,0)), Player(100,100,50,50,(0,0,255))]

def threaded_client(cnx, player):
    cnx.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(cnx.recv(2048))
            players[player] = data

            if not data:
                print('Disconnected')
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("recieved: ", data)
                print("sending : ", reply)
                
            cnx.sendall(pickle.dumps(reply))
        except:
            break
        
    print("lost connection")
    cnx.close()

currentPlayer = 0
while True:
    cnx, addr = s.accept()
    print("connected to : ", addr)

    start_new_thread(threaded_client, (cnx, currentPlayer))
    currentPlayer += 1






