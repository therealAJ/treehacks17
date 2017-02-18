import serial
ser = serial.Serial('/dev/cu.usbserial-AI03Y56G', 9600)

while True:
    print(ser.readline())
