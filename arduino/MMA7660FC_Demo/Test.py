import serial
ser = serial.Serial('/dev/cu.usbserial-AI03Y56G', 9600)

while True:
    line = ser.readline()
    if 'accleration' in str(line):
        v = []
        for _ in range(3):
            line = ser.readline()
            end = 7 if '-' in str(line) else 6
            val = float(str(line)[2:end])
            v.append(val)
        print(v)
