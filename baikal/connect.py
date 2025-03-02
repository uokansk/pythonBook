import socket
import pickle
import time

hostAddress = 'A8:93:4A:CE:63:28'

channel = 4
backlog = 1
mySocket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
mySocket.bind((hostAddress, channel))
print("проверка работы клиента")
mySocket.listen()
print("соединение...")
client, address = mySocket.accept()
while True:
    a = int(input("вводите"))
    dataToSend = a
    bytesToSend = pickle.dumps(dataToSend)  # преобразование данных в байтовую систему для EV3
    print(a)
    client.send(bytesToSend)  # отправка данных в модуль EV3
