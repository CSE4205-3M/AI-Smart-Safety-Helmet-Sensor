import smbus
import time
import pandas as pd
from math import abs
bus = smbus.SMBus(0)

address = 0x53

x_adr = 0x32
y_adr = 0x34
z_adr = 0x36
pre_x = 0
pre_y = 0
pre_z = 0

def init_ADXL345():
    bus.write_byte_data(address, 0x2D, 0x08)

def measure_acc(adr):
    acc0 = bus.read_byte_data(address, adr)
    acc1 = bus.read_byte_data(address, adr + 1)

    acc = (acc1 << 8) + acc0
    if acc > 0x1FF:
        acc = (65536 - acc) * -1

    return acc

try:
    init_ADXL345()

    while True:
        x_acc = measure_acc(x_adr)
        y_acc = measure_acc(y_adr)
        z_acc = measure_acc(z_adr)
        
        pre_x = x_acc
        pre_y = y_acc
        pre_z = z_acc
    
        if abs(pre_x - x_acc) > 500 and 
        print(f"X-Axis: {x_acc}, Y-Axis: {y_acc}, Z-Axis: {z_acc}")
        
        time.sleep(0.5)

except KeyboardInterrupt:
    pass
