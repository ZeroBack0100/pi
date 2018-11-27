import serial
ser = serial.Serial("/dev/ttyAMA0")
ser.baudrate = 9600
data = ser.read()
ser.write(data)
ser.close()
