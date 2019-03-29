#!/usr/bin/python3
from IoTSupport import LogDebug
#import RPi.gpio as gpio
from gpiozero import LED, CPUTemperature, MotionSensor, MCP3008, OutputDevice
from time import sleep
from signal import pause

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
        if self.stepCounter_ >= self.stepCount_:
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

def motion_detected():
    LogDebug("M Detected")
def Test_MOTION(motion, led):
    LogDebug(motion.pin)
    LogDebug(motion.value);
    motion.wait_for_motion()
    LogDebug("motion detected")
    LogDebug(motion.value);
    motion.when_motion = led.on
    motion.when_no_motion = led.off
    #motion.when_motion = motion_detected
    #while True:
    #    #LogDebug("Ready");
    #    if motion.motion_detected:
    #        LogDebug("motion detected")
    pause()
    
def Test_LED(led):
    LogDebug(led.pin)
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)
if __name__ == '__main__':
    LogDebug("Sensors Called.")
    #gpio.write(13, 0)
    sensor = Sensors()
    led = sensor.led()
    motion =  sensor.motion()
    #led.blink()
    Test_MOTION(motion, led)
    pause()
    #while True:
    #    led.on()
    #    sleep (1)
    #    led.off()
    #    sleep(1)
    #led.on()
    #LogDebug(sensor.motion().pin);
    #LogDebug(sensor.motion().value);
    #LogDebug(sensor.current().value);
    #LogDebug(sensor.cpu().temperature)
    #LogDebug(sensor.cpu().value)
