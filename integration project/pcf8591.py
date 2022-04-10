#!/usr/bin/python
import smbus
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
address = 0x48

A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43

bus = smbus.SMBus(1)

def readValue():
    return bus.write_byte(address,A0)

def main():
	try:
		while True:
		    bus.write_byte(address,A0)
		    value = bus.read_byte(address)
		    print("Value: %s" % value)
		    time.sleep(0.1)
	except KeyboardInterrupt:
	    GPIO.cleanup()

if __name__ == "__main__":
	main()
