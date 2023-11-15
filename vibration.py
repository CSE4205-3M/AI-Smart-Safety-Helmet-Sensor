import spidev
import time
from math import abs
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1350000
pre_reading = 1024
def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1] & 3) << 8) + r[2]
    return adc_out

try:
	while True:
		reading = analog_read(0)
		if abs(pre_reading - reading) > 200:
			
		print("Vibration analog value: ", reading)
		time.sleep(0.05)
		
except KeyboardInterrupt:
	spi.close()
	print("SPI closed.")
