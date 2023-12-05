import serial
import pynmea2

def parseGPS(st):
    result = st.decode('utf-8')
    if 'GGA' in result:
	    msg = pynmea2.parse(result)
	    print(f"Timestamp: {msg.timestamp} Latitude: {msg.lat}, Longitude: {msg.lon}")
	    #print(f"Timestamp: {msg.timestamp} -- Lat: {msg.lat} {msg.lat_dir} -- Lon: {msg.lon} {msg.lon_dir} -- Altitude: {msg.altitude} {msg.altitude_units}")
serialPort = serial.Serial("/dev/serial0", 9600, timeout=0.5)
while True:
    str = serialPort.readline()
    parseGPS(str)
