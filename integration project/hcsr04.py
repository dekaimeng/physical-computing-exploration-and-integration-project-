import RPi.GPIO as GPIO
import time

Trig_Pin =19 
Echo_Pin = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Trig_Pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(Echo_Pin, GPIO.IN)

time.sleep(2)

def checkdist():
    GPIO.output(Trig_Pin, GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(Trig_Pin, GPIO.LOW)
    while not GPIO.input(Echo_Pin):
        pass
    t1 = time.time()
    while GPIO.input(Echo_Pin):
        pass
    t2 = time.time()
    return (t2-t1)*340*100/2

def submain():
	i = 0
	try:
	    while i < 5:
			i = i + 1
			print i
			print 'Distance:%0.2f cm' % checkdist()
			time.sleep(1)
	except KeyboardInterrupt:
	    GPIO.cleanup()
def main():
	try:
	    while True:
	        print 'Distance:%0.2f cm' % checkdist()
	        time.sleep(1)
	except KeyboardInterrupt:
	    GPIO.cleanup()

if __name__ == "__main__":
	main()
 
