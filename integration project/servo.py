#!/usr/bin/python

from __future__ import division 
import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
class sg90:

  def __init__( self, direction):

    self.pin = 23
    GPIO.setmode( GPIO.BCM )
    GPIO.setup( self.pin, GPIO.OUT )
    self.direction = int( direction )
    self.servo = GPIO.PWM( self.pin, 50 )
    self.servo.start(0.0)

  def cleanup( self ):

    self.servo.ChangeDutyCycle(self._henkan(0))
    time.sleep(0.3)
    self.servo.stop()
    GPIO.cleanup()

  def currentdirection( self ):

    return self.direction

  def _henkan( self, value ):

    return 0.05 * value + 7.0

  def setdirection( self, direction, speed ):

    for d in range( self.direction, direction, int(speed) ):
      self.servo.ChangeDutyCycle( self._henkan( d ) )
      self.direction = d
      time.sleep(0.1)
    self.servo.ChangeDutyCycle( self._henkan( direction ) )
    self.direction = direction

  def rotate(self, degree):
		deg = -90 + 200 * degree / 180
		self.setdirection(int(deg), 20)

def main():
	s = sg90(0)
	try:
		while True:
			print("0")
			s.rotate(0)
			time.sleep(6.5)

			print("30")
			s.rotate(30)
			time.sleep(4.5)

			print("60")
			s.rotate(60)
			time.sleep(4.5)


			print("100")
			s.rotate(100)
			time.sleep(6.5)

			print("130")
			s.rotate(130)
			time.sleep(4.5)

			print("150")
			s.rotate(150)
			time.sleep(4.5)

			print("180")
			s.rotate(180)
			time.sleep(6.5)
	except KeyboardInterrupt:
		s.cleanup()

if __name__ == "__main__":
    main()
