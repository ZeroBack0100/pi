import time as ti
import serial
import pynmea2
import datetime
import sys
import requests

try:
    name = sys.argv[1]
except:
    print(">> python3", sys.argv[0], "name")
    exit()

url = 'http://yhs3434.pythonanywhere.com/gps/'
port = "/dev/ttyUSB0"
ser = serial.Serial(port, baudrate=9600, timeout=0.5)

params = {}

print("wait...")

while (True):
    params = {}
    newdata = ser.readline().decode("UTF-8")
    if(newdata[0:6] == '$GPGGA'):
        newmsg = pynmea2.parse(newdata)
        time = datetime.datetime.now()
        lat = newmsg.latitude
        lon = newmsg.longitude

        params['name'] = name
        params['latitude'] = lat
        params['longitude'] = lon
        try:
            res = requests.post(url, json=params)
        except:
            continue

        print(time.strftime('%Y-%m-%d %H:%M:%S'), lat, lon)
        ti.sleep(30)
