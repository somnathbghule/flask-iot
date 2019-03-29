#!/usr/bin/env python3

import RPi.GPIO as GPIO
import sys
sys.path.append("/usr/local/lib/python3.5/dist-packages/mfrc522")
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()
