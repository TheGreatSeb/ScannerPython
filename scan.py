import cv2
import pyzbar.pyzbar as pyzbar
from datetime import datetime
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket.connect(("127.0.0.1",9090));

#width = 2592
#height = 100

camera = cv2.VideoCapture(0)
#camera.set(3,width)
#camera.set(4,height)

def decodeCam(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    codes = pyzbar.decode(gray)
    print('reading...', end='\r')
    for code in codes:
        codeData = code.data.decode()
        codeType = code.type
        #print("["+str(datetime.now())+"] Type:{} | Data: {}".format(codeType, codeData))
        print(codeData, codeType)
        with open("/home/master/eksamensprojekt/nummer.txt") as f:
            contents = f.read()
        clientSocket.send(codeData.encode('utf8'))
        clientSocket.send(contents.encode('utf8'))
        print("Send.. Exiting.. 👋")
        exit()
    return image

try:
 while True:
  ret, frame = camera.read()
  im=decodeCam(frame)

except KeyboardInterrupt:
 print('interrupted! 🚨')
