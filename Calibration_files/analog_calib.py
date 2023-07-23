import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class analogue_ada_sensor(object):
    #Adafruit pins
    pins = {
        0: ADS.P0,
        1: ADS.P1,
        2: ADS.P2,
        3: ADS.P3
    }

    def __init__(self, type_of_data, pin):
        self.type_of_data = type_of_data
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.digital_converter = ADS.ADS1015(self.i2c)

        if pin not in [0, 1, 2, 3]:
            raise ValueError("Invalid pin. Please input a valid pin number (0, 1, 2, or 3).")
        self.channel = AnalogIn(self.digital_converter, self.pins[pin])  # The channel value will be ADS.PX (P0-P3)

    def get_signal_converter(self):
        return self.signal_converter

    def get_channel(self):
        return self.channel

    def get_voltage(self):
        return self.channel.voltage  # Returns the voltage value

    def get_raw_value(self):
        return self.channel.value  # Returns the raw ADC value

    def __str__(self):
        return f"Analog Sensor (Type: {self.type_of_data}, Pin: {self.channel.name}, Voltage: {self.get_voltage():.2f}V)"

    
## calibrating the sensor get the sun value
## recommended that there is an open air and wet control value for moisture sensor
##
def get_control_value(sensor, Time): #argument must be the analogue_ada_sensor type and the seconds
    control_values = []
    
    count = 0
    while count < Time:
        sensor_value = sensor.get_raw_value()
        control_values.append(sensor_value)
        print(f"raw data value: {sensor_value}")
        count+=1
        time.sleep(1) #get reading per second

        
    return max(control_values)

##based on arduino map() function
def mapValue(sensor_value, min_value, max_value, mappedLow, mappedHigh):
        return ((sensor_value - min_value) * (mappedHigh - mappedLow)) / (max_value - min_value) + mappedLow


###testing




