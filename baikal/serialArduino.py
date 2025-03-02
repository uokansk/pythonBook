import serial
import time
arduino= serial.Serial('com6', 9600)
time.sleep(2)
print('Connect')

while True:
    e = input('enter komand')
    i=e.encode()
    arduino.write(i)
