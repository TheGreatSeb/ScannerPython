#----- A simple TCP based server program in Python using send() function -----
import socket
import csv

# Create a stream based socket(i.e, a TCP socket)
# operating on IPv4 addressing scheme
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
# Bind and listen
host = "127.0.0.1"
port = 9090
print ("Host: ", host)
print ("Port: ", port)
print ("--💀-- Ready to receive data --💀--")
serverSocket.bind((host, port))
serverSocket.listen();

# Accept connections
while(True):
    (clientConnected, clientAddress) = serverSocket.accept();
    print("Client connected %s:%s"%(clientAddress[0], clientAddress[1]));
    dataFromClient = clientConnected.recv(1024)
    data2FromClient = clientConnected.recv(1024)
    print(dataFromClient.decode());
    print(data2FromClient.decode());
    row=[dataFromClient.decode(),data2FromClient.decode()]
    with open('/home/master/eksamensprojekt/products.csv','a') as csvFile:   #a to append to existing csv file
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
    print("--💀-- Done --💀--")
    # Send some data back to the client