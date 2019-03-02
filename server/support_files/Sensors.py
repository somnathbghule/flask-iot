#!/usr/bin/python3
from IoTSupport import LogDebug
from gpiozero import LED

class Sensor():
    def __init__(self):
        LogDebug("Sensor __init__ called.")

class PIR(Sensor):
    def __init__(self):
        LogDebug("PIR __init__ called.")
        super().__init__();
        
if __name__ == '__main__':
    LogDebug("Sensors Called.")
    pir=PIR()
