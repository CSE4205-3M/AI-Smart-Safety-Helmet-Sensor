# acc
import smbus
import time
from collections import deque

# vib
import spidev

# API
import requests
import json


def send_api(path, method, desc):
	API_HOST = "http://165.246.44.237:11108/"
	url = API_HOST + path
	headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
	body = {
		"latitude": 0,
		"longitude": 0,
		"raspberryPiId": "10",
		"value": 1,
		"description": desc
	}
	
	try:
		if method =='GET':
			response = requests.get(url, headers=headers)
		elif method == 'POST':
			response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent='\t'))
	except Exception as ex:
		print(ex)

# acc

bus = smbus.SMBus(0)

address = 0x53

x_adr = 0x32
y_adr = 0x34
z_adr = 0x36
pre_x = deque()


def init_ADXL345():
    bus.write_byte_data(address, 0x2D, 0x08)

def measure_acc(adr):
    acc0 = bus.read_byte_data(address, adr)
    acc1 = bus.read_byte_data(address, adr + 1)

    acc = (acc1 << 8) + acc0
    if acc > 0x1FF:
        acc = (65536 - acc) * -1

    return acc

# vib

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1350000
pre_reading = 1024

def analog_read(channel):
	r = spi.xfer2([1, (8 + channel) << 4, 0])
	adc_out = ((r[1] & 3) << 8) + r[2]
	return adc_out

# acc + vib

try:
    init_ADXL345()
    while True:
        reading = analog_read(0)
        print("Vibration analog value: ", reading)
		
        x_acc = measure_acc(x_adr)
        y_acc = measure_acc(y_adr)
        z_acc = measure_acc(z_adr)
        if len(pre_x) == 10:
            pre_x.popleft()
        pre_x.append(x_acc)
        if pre_reading - reading > 300:
            if abs(pre_x[0] - x_acc) > 200:
                send_api('accident/workerAccident', 'POST', "Falling accident Occured.")
            else:
                send_api('accident/workerAccident', 'POST', "Collsion Accident Occured.")


        pre_reading = reading
        print(f"X-Axis: {x_acc}, Y-Axis: {y_acc}, Z-Axis: {z_acc}")
        
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
