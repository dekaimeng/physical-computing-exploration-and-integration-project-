import servo as servo 
import dig1 as dig
import hcsr04 as ultra 
import pcf8591 as potent 
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
str1 = "0"
str2 = "0"
shower = dig.Segment() 
servoInstance = servo.sg90(0)
shower.show_number(0)
try:
	while True:
		print("1.sumaguan")
		print("2.servo")
		print("3.distance")
		print("4.dianweiqi")
		print("5.total")
		str1 = raw_input("please input you chioce, over is exit:")
		chioceNum = int(str1)
		if(chioceNum == 1):
			dig.main()
		elif (chioceNum == 2):
			shower.show_number(2)
			servo.main()
		elif (chioceNum == 3):
			shower.show_number(3)
			ultra.submain()
		elif (chioceNum == 4):
			shower.show_number(4)
			potent.main()
		elif (chioceNum == 5):
			shower.show_number(5)
			try:
				while true:
					str2 = raw_input("please input you angle, over is exit:")
					angle = int(str2)
					servoInstance.rotate(angle)
					if (str2 == 'over'):
						str2 = '0'
						shower.show_number(0)
						GPIO.cleanup()
						break
			except KeyboardInterrupt:
                print('aa')

		if (str1 == 'over'):
			str1 = "0"
			shower.show_number(0)
			GPIO.cleanup()
			break
finally:
	GPIO.cleanup()

