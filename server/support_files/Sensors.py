#!/usr/bin/python3
from IoTSupport import LogDebug
from gpiozero import LED, CPUTemperature, MotionSensor, MCP3008

class Sensors():
    def __init__(self):
        self.gpioPins_ = {
            'led':5,
            'pir1':13,
            'pir2':17
        }
        self.led_ = LED(self.gpioPins_['led']) #for LED
        self.motion_ = MotionSensor(self.gpioPins_['pir1'])  #for PIR1
        self.curret_ = MCP3008(channel=0)  #ACS 11
        self.cpu_ = CPUTemperature(min_temp=50, max_temp=90) #CPU Info
    def led(self):
        return self.led_
    def motion(self):
        return self.motion_;
    def current(self):
        return self.curret_;
    def cpu(self):
        return self.cpu_;
        
if __name__ == '__main__':
    LogDebug("Sensors Called.")
    sensor=Sensors()
    #LogDebug(sensor.led().pin);
    #LogDebug(sensor.motion().pin);
    #LogDebug(sensor.motion().value);
    #LogDebug(sensor.current().value);
    LogDebug(sensor.cpu().temperature)
    LogDebug(sensor.cpu().value)
