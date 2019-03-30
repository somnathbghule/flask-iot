#!/usr/bin/python3
from IoTSupport import LogDebug
from gpiozero import LED, CPUTemperature, MotionSensor, MCP3008, OutputDevice, MCP3008

gpioPins = {
    'LED':5,
    'PIR1':13,
    'PIR2':27,
    'MOTORIN1':17,
    'MOTORIN2':22,
    'MOTORIN3':23,
    'MOTORIN4':24
}
        
class StepperMotor():
    def __init__(self,stepDir, mode):
        self.stepPins_=[OutputDevice(gpios['MOTORIN1']), OutputDevice(gpioPins['MOTORIN2']),
        OutputDevice(gpioPins['MOTORIN3']), OutputDevice(gpioPins['MOTORIN4'])]
        self.stepDir_=stepDir #Set 1 for clockwise
        self.mode_ = mode  # mode = 1: Low Speed ==> Higher Power # mode = 0: High Speed ==> Lower Power
        self.stepCount=len(sequence())
        self.stepCounter_=0
    def clockwise(self):
        self.stepDir_=1

    def mode(self):
        return self.mode_
    def incSpeed(self):
        self.mode_=1

    def decSpeed(self):
        self.mode_=0

    def sequence(self):
        if self.mode(): #low speed to high speed
            seq=[[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]
            return seq
    def accelerate(self, speed):
        self.waitTime_=speed
        
    def run(self):
        for pin in range(0, 4):
            xPins=self.stepPins_[pin]
            if self.sequence()[self.stepCounter_][pin] != 0:
                xPin.on()
            else:
                xPin.off()
        self.stepCounter += self.stepDir
        if self.stepCounter_ > = self.stepCount_:
            self.stepCounter_ = 0
        if self.stepCounter_ < 0 :
            self.stepCounter_=self.stepCount_+self.stepDir_
        time.sleep(self.waitTime_)
        
class Sensors():
    def __init__(self):
        self.led_ = LED(gpioPins['LED']) #for LED
        self.motion_ = MotionSensor(gpioPins['PIR1'])  #for PIR1
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
