##Testing the DHT sensor
from Sensors_devices.myDHT22 import DHT
import time



while True:
    myDHT = DHT(4, "DHT22")
    #humidity, temperature = myDHT.get_results()
    print(myDHT.get_results())
    #print("Temperature = {:1.1f}*C".format(temperature) + " Humidity = {:1.1f}%".format(humidity))
    time.sleep(3)