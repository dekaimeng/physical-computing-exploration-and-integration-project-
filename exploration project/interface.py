import RPi.GPIO as GPIO
import LCD1602 as LCD
import Remote as remote

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

str1 = "0"
str2 = "0"
try:
    while True:
        print("1.remote")
        print("2.lcd")
        print("3.remote control lcd")
        str1 = raw_input("please input you chioce, over is exit:")
        if str1 == 'over':
            str1 = "0"
            GPIO.setmode(GPIO.BCM)
            GPIO.cleanup()
            break
        chioceNum = int(str1)
        if chioceNum == 1:
            remote.main()
        elif chioceNum == 2:
            LCD.main()
        elif chioceNum == 3:
            remote.remote_lcd_main()
finally:
    GPIO.cleanup()
