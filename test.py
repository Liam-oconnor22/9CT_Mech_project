from machine import ADC, Pin
import math
import time

# Pass the Pin object into the ADC constructor
temp_adc = ADC(26)

beta = 3950.0
r0 = 10000.0
t0 = 25.0 + 273.15
r_fixed = 10000.0

def read_temp():
    raw_temp = temp_adc.read_u16()
    if raw_temp == 0:
        raw_temp = 1
        
    voltage = raw_temp * 3.3 / 65535.0
    resistance = (voltage * r_fixed) / (3.3 - voltage)
    steinhart_eq = math.log(resistance / r0) / beta
    steinhart_eq += 1.0 / t0
    kelvin = 1.0 / steinhart_eq
    celcius = kelvin - 273.15
    print(celcius)
    return celcius

while True:
    read_temp()
    time.sleep(1)
