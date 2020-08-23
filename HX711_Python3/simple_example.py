#!/usr/local/bin/python
from pyA20.gpio import gpio
from pyA20.gpio import port
from hx711 import HX711  # import the class HX711

hx = HX711(dout_pin=port.PA6, pd_sck_pin=port.PA3)  # create an object
while(True):
    print(hx.get_raw_data_mean())  # get raw data reading from hx711
