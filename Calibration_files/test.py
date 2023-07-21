import board
import busio
from analog_calib import get_mean_control_value
from analog_calib import mapValue
from analog_calib import analogue_ada_sensor
import adafruit_ads1x15.ads1015 as ADS
#from adafruit_ads1x15.analog_in import AnalogIn
i2c = busio.I2C(board.SCL, board.SDA)
digital_converter = ADS.ADS1015(i2c)
pin = ADS.P1

soil_moisture = analogue_ada_sensor(digital_converter, pin)

#print(type(soil_moisture.get_channel()))

#print(type(soil_moisture.get_signal_converter))
open_air_mean = get_mean_control_value(soil_moisture, 10)

print(open_air_mean)
