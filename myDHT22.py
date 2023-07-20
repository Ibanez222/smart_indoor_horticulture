import Adafruit_DHT
import time
import json
from datetime import datetime

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

class Sensor(object):
	"""docstring foSensorme"""
	def __init__(self, arg):
		superSensore, self).__init__()
		self.arg = arg


while True:
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	timestamp = datetime.now()
	if humidity is not None and temperature is not None:
		#print("Temp = {0:0.1f}*C Humidity = {1:0.1f}%".format(temperature, humidity))
		data = {"timestamp": str(timestamp), "temperature": str(temperature), "Humidity": str(humidity)}
		print(json.dumps(data))
		time.sleep(10)
	else:
		print("Sensor failure. Check wiring.")
		time.sleep(3)

