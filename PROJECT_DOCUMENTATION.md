# 9CT_Mech_project


# Requirement Outline

### Problem: 

Temperatures reach too high of a level within rooms with bad ventilation while unmonitored which could kill organic life (such as plants or animals kept in the room). This is seen with animals trapped inside cars without airconditioning or just cars with their power off.


### The solution:
Building a temperature sensing device that activates a fan when the temperature reaches a certain level and disables it once it reaches the desired temperature. For example if an animal is within a turned off car unnattended, if the temperature goes above 22 degrees celsius, the fan will turn on and stay on until the temperature is stable again.


### Key actions:
1- Temperature exceeds 22 degrees.
2- Temperature sensor gathers info which is then processed by the raspberry pi pico and turned into understandable information .
3- Raspberry pi pico then checks if this temperature is above or below 22 degrees .
4- since the temperature exceeds 22 degrees, it activates the fan.
5- The fan reaches max acceleration and cools down the area.

Functional requirements:
Temperature sensor input- if temperature is >= 22 then turn on the fan until the temperature drops below 22 degrees.
Fan - must turn on when temperature is above or equal to 22, and turn off when it falls below 22.



### Test Cases

| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Temperature above 22 degrees     |           |         The fan activates and cools down the room/ car to desired temperature ( below 22 degrees celcius)          |
|           |           |                   |
|           |           |                   |


### Non functional requirements

reaction time- must be within 1 second to ensure safety 

accuracy- temperature must be accurate to the degree as even 1 degree wrong could risk safety

efficiency- fan speed is efficient enough to reliably cool downb a large space in time.