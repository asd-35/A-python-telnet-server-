import socket
import threading
import datetime
from zeep import Client
import os

client = Client(wsdl="http://localhost:51479/WebService1.asmx?wsdl")


BYTE = 6 # server uses utf-8 as formatting since telnet client sends one char at a time using the biggest size of byting of a char for streaming data seemed fine rather than using 1024 bytes like in every site
# i know we dont trade a lot of bytes but streaming 6  bytes is faster than 1024 bytes
PORT = 7777
SERVER = socket.gethostbyname(socket.gethostname()) # built-in method to fetch ip of the machine that codes running
ADDR = (SERVER, PORT) # putting server and port number into a tuple
FORMAT = "utf-8"




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a socket
server.bind(ADDR) #binding the socket with the address





def handle_client(conn,addr): # in this block of code i handle all the clients that connects  to our server
    print(f"{addr} connected") #ip of the client printed
    connected = True
    conn.send("Hello welcome to the server you can convert your favourite decimal number into hex , octal and binary\r\n".encode(FORMAT))

    msg_full = ""
    conn.send("Commands are (hex + your desired number,octal + your desired number,binary + your desired number)\r\n".encode(FORMAT))#printing commands


    while connected:# after they connect with a while loop we let them ask stuff as much as we want
        msg=conn.recv(BYTE).decode(FORMAT)
        msg_full += str(msg)
        if msg == "\r\n":
            if msg_full == "quit\r\n": #kills the connection between client
                print(f"-- {addr} -- > {msg_full}")

                conn.send("Bye Bye\r\n".encode(FORMAT))
                connected = False
                conn.close()
            elif "hex" in msg_full and msg_full[:3] == "hex" :
                print(f"-- {addr} -- > {msg_full}")
                result = client.service.convertHex(int(msg_full[3:])) + "\r\n"
                msg_full= ""
                conn.send(result.encode(FORMAT))
            elif "octal" in msg_full and msg_full[:5] == "octal":
                print(f"-- {addr} -- > {msg_full}")
                result = client.service.convertOctal(int(msg_full[5:])) + "\r\n"
                msg_full = ""
                conn.send(result.encode(FORMAT))
            elif "binary" in msg_full and msg_full[:6] == "binary":
                print(f"-- {addr} -- > {msg_full}")
                result = client.service.convertBinary(int(msg_full[6:])) + "\r\n"
                msg_full = ""
                conn.send(result.encode(FORMAT))
            else:
                print(f"-- {addr} -- > {msg_full}")
                msg_full = ""
                conn.send("It is not a valid command please enter a valid command\r\n".encode(FORMAT))



def start(): #starts the server and it also treats clients as threads it makes it multi connectiable(to be honest i dont know if multi connectiable is a word :D )
    server.listen() #starts listening on 555
    print(f"its listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr)) #every client connection goes to be a thread under the control of the handle_client function
        thread.start()#they run here
        print(f"The number of client(s) connected : {threading.activeCount()- 1}") # active users connected to the server you can limit it with few codes

print("server is starting...")
start() #server starting