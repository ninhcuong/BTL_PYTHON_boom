
import socket
 
   
HOST = "192.168.184.170"
SERVER_PORT = 65432
FORMAT ="utf8"
 
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,SERVER_PORT))
s.listen()
 
print("server:",HOST,SERVER_PORT)
print("Waiting...")
 
while 1:
    conn, addr = s.accept()
 
    print("!Client connected!")
    print("client address:",addr)
    print("conn:", conn.getsockname())






import socket
 
HOST = "192.168.184.170"
SERVER_PORT = 65432
FORMAT ="utf8"
 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
client.connect( (HOST, SERVER_PORT))
 
print("!Connected to the server!")

