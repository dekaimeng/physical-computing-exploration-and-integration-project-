import RPi.GPIO as GPIO
import IRModule
import time
import LCD1602 as lcd

# remote callback function
def remote_callback(code):
    if code == 16738455:  # Button 0
        print("key0")

    if code == 16724175:  # Button 1
        print("key1")

    if code == 16718055:  # Button 2
        print("key2")

    if code == 16743045:  # Button 3
        print("key3")

    if code == 16716015:  # Button 4
        print("key4")

    if code == 16726215:  # Button 5
        print("key5")

    if code == 16734885:  # Button 6
        print("key6")

    if code == 16728765:  # Button 7
        print("key7")

    if code == 16730805:  # Button 8
        print("key8")
    if code == 16732845:  # Button 9
        print("key9")

    if code == 16750695:  # Button 100+
        print("key 100+")

    if code == 16756815:  # Button 200+
        print("key 200+")

    if code == 16720605:  # Button <<
        print("key <<")

    if code == 16712445:  # Button >>
        print("key >>")

    if code == 16761405:  # Button >||
        print("key >||")

    if code == 16769055:  # Button -
        print("key -")

    if code == 16754775:  # Button +
        print("key +")

    if code == 16736925:  # Button CH
        print("key CH")

    if code == 16769565:  # Button CH+
        print("key CH+")

    if code == 16753245:  # Button CH-
        print("key CH-")

    if code == 16748655:  # Button EQ
        print("key EQ")

    print(str(code))
    return

# lcd remote terminal callback function
def lcd_remote_callback(code):
    if code == 16738455:  # Button 0
        print("key0")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key0")

    if code == 16724175:  # Button 1
        print("key1")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key1")

    if code == 16718055:  # Button 2
        print("key2")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key2")

    if code == 16743045:  # Button 3
        print("key3")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key3")

    if code == 16716015:  # Button 4
        print("key4")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key4")

    if code == 16726215:  # Button 5
        print("key5")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key5")

    if code == 16734885:  # Button 6
        print("key6")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key6")

    if code == 16728765:  # Button 7
        print("key7")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key7")

    if code == 16730805:  # Button 8
        print("key8")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key8")
    if code == 16732845:  # Button 9
        print("key9")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key9")

    if code == 16750695:  # Button 100+
        print("key 100+")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key 100+")

    if code == 16756815:  # Button 200+
        print("key 200+")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key 200+")

    if code == 16720605:  # Button <<
        print("key <<")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key <<")

    if code == 16712445:  # Button >>
        print("key >>")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key >>")

    if code == 16761405:  # Button >||
        print("key >||")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key >||")

    if code == 16769055:  # Button -
        print("key -")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key >||")

    if code == 16754775:  # Button +
        print("key +")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key +")

    if code == 16736925:  # Button CH
        print("key CH")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key CH")

    if code == 16769565:  # Button CH+
        print("key CH+")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key CH+")

    if code == 16753245:  # Button CH-
        print("key CH-")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key CH-")

    if code == 16748655:  # Button EQ
        print("key EQ")
        lcd.clear_lcd()
        lcd.print_lcd(0, 0, "key EQ")

    print(str(code))
    return

# remote lcd terminal control main function
def remote_lcd_main():
    irPin = 16
    ir = IRModule.IRRemote(callback='DECODE')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)  # uses numbering outside circles
    GPIO.setup(irPin, GPIO.IN)  # set irPin to input
    GPIO.add_event_detect(irPin, GPIO.BOTH, callback=ir.pWidth)

    try:
        ir.set_callback(lcd_remote_callback)

        while True:
            time.sleep(1)

    except KeyboardInterrupt:  # trap a CTRL+C keyboard interrupt
        print('Removing callback and cleaning up GPIO')
        ir.remove_callback()
        GPIO.cleanup()

# remote main function
def main():
    irPin = 16
    ir = IRModule.IRRemote(callback='DECODE')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)  # uses numbering outside circles
    GPIO.setup(irPin, GPIO.IN)  # set irPin to input
    GPIO.add_event_detect(irPin, GPIO.BOTH, callback=ir.pWidth)

    try:
        ir.set_callback(remote_callback)

        while True:
            time.sleep(1)

    except KeyboardInterrupt:  # trap a CTRL+C keyboard interrupt
        print('Removing callback and cleaning up GPIO')
        ir.remove_callback()
        GPIO.cleanup()


if __name__ == '__main__':
    main()
