from machine import Pin, ADC
import math
import time

temp_adc = ADC(26)

beta = 3950.0
r0 = 10000.0
t0 = 25.0 + 273.15
r_fixed = 10000.0

def read_temp():
    raw_temp = temp_adc.read_16()
        if raw_temp == 0:
            raw_temp = 1
            
        # raw_temp value multiplied by ADC voltage then divided by the max raw digital value 
        voltage = raw_temp * 3.3/65535.0
        
        resistance = (voltage * r_fixed) / (3.3 - voltage)
        
        steinhart_eq = math.log(resistance / r0) / beta
        steinhart_eq += 1.0 / t0
        kelvin = 1.0 / steinhart_eq
        
        celcius = kelvin - 273.15
        return celcius
    
    
while True:
  temp_c = read_temperature()
  print(f"Temperature: {temp_c} degrees Celcius")
  sleep(1)
  if temp_c >= 22:
      fan = turn on
    