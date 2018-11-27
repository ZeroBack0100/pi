import serial

# Maybe, you should change a port.
ser = serial.Serial(
        port = '/dev/ttyACM0',
        baudrate = 9600,
)

while (True):
    if ser.readable():
        line = ser.readline()
        print(line.decode()[:len(line)-1])
