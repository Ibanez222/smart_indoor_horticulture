import Adafruit_DHT
import time
import json
from datetime import datetime



class DHT(object):
	def __init__(self, pin, model):
		self.pin = pin
		self.model = model

	def get_pin(self):
		return self.pin
	
	def get_model(self):
		return self.model
	
	def get_results(self): #This method returns a tuple which contains the (humidity, temp) readings
		return Adafruit_DHT.read_retry(self.model, self.pin)




'''
sensor = DHT(4, Adafruit_DHT.DHT22)	

while True:
	humidity, temperature = sensor.get_results()
	timestamp = datetime.now()
	if humidity is not None and temperature is not None:
		#print("Temp = {0:0.1f}*C Humidity = {1:0.1f}%".format(temperature, humidity))
		data = {"timestamp": str(timestamp), "temperature": str(temperature), "Humidity": str(humidity)}
		print(json.dumps(data))
		time.sleep(10)
	else:
		print("Sensor failure. Check wiring.")
		time.sleep(3)
'''
