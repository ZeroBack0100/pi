import serial
import time

STOP = '5'
FRONT = '2'
LEFT = '4'
RIGHT = '1'
BACK = '3'

# Connect priority :  Motor -> Bluetooth

# raspberry pi -> arduino(motor)
ser_out = serial.Serial(
        port = '/dev/ttyACM0',
        baudrate = 9600,
        )

# arduino(bluetooth) -> raspberry pi
ser_in = serial.Serial(
        port = '/dev/ttyACM1',
        baudrate=9600,
        )

def move(ser, position, distance):
    dist = int(round(distance))
    if (position == FRONT):
        ser.write(FRONT.encode())
        time.sleep(int(dist*1.5))
        ser.write(STOP.encode())
    elif (position == LEFT):
        ser.write(LEFT.encode())
        time.sleep(1)
        ser.write(STOP.encode())
        time.sleep(1)
    elif (position == RIGHT):
        ser.write(RIGHT.encode())
        time.sleep(1)
        ser.write(STOP.encode())
        time.sleep(1)

print ('Waiting...')

while (True):
    if ser_in.readable():
        line = ser_in.readline()
        line = line.decode()
        print(line)

        # manual moving
        if(line[0]=='c'):
            try:
                pos = line[1]
                ser_out.write(pos.encode())
            except:
                print("Control error")
        # Set the position to go.
        #
        #
        else:
            beacon_id_str = line[0]
            beacon_distance_str = line[2:5]
            try:
                beacon_id = int(beacon_id_str)
                beacon_distance = float(beacon_distance_str)
            except:
                print('The value is wrong...', line)
            else:
                try:
                    if(beacon_id == 0):
                        print('front', beacon_id_str, beacon_distance_str)
                        move(ser_out, FRONT, beacon_distance)
                    elif (beacon_id == 1):
                        print('left', beacon_id_str, beacon_distance_str)
                        move(ser_out, LEFT, beacon_distance)
                    elif (beacon_id == 2):
                        print('right', beacon_id_str, beacon_distance_str)
                        move(ser_out, RIGHT, beacon_distance)
                    ser_in.flushInput()
                    ser_in.flushOutput()
                    ser_out.flushInput()
                    ser_out.flushOutput()
                except:
                    print("error")
#               if(type(wr) is str):
#                    ser_out.write(wr.encode())
#               elif(type(wr) is bytes):
#                   ser_out.write(wr)

