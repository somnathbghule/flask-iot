#!/usr/bin/python3
#!/usr/bin/env python3

import RPi.GPIO as GPIO
import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages/mfrc522/')
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        text = input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
finally:
        GPIO.cleanup()
