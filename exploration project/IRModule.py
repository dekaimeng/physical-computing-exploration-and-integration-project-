#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time, threading


class IRRemote:

    def __init__(self, callback=None):

        self.decoding = False
        self.pList = []
        self.timer = time.time()
        if callback == 'DECODE':
            self.callback = self.print_ir_code
        else:
            self.callback = callback
        self.checkTime = 150  # time in milliseconds
        self.verbose = False

    def pWidth(self, pin):
        """pWidth, function to record the width of the highs and lows
        of the IR remote signal and start the function to look for the
        end of the IR remote signal"""

        self.pList.append(time.time() - self.timer)
        self.timer = time.time()

        if self.decoding == False:
            self.decoding = True
            check_loop = threading.Thread(name='self.pulse_checker', target=self.pulse_checker)
            check_loop.start()

        return

    def pulse_checker(self):
        """pulse_checker, function to look for the end of the IR remote
        signal and activate the signal decode function followed by
        the callback function."""

        while True:
            check = (time.time() - self.timer) * 1000
            if check > self.checkTime:
                # print(check)
                break
            time.sleep(0.01)

        decode = self.decode_pulse(self.pList)

        self.pList = []
        self.decoding = False

        if self.callback != None:
            self.callback(decode)

        return

    def decode_pulse(self, pList):
        """decode_pulse,  function to decode the high and low
        timespans captured by the pWidth function into a binary
        number"""

        bitList = []
        sIndex = -1

        # convert the timespans in seconds to milli-seconds
        # look for the start of the IR remote signal

        for p in range(0, len(pList)):
            try:
                pList[p] = float(pList[p]) * 1000
                if self.verbose == True:
                    print(pList[p])
                if pList[p] < 11:
                    if sIndex == -1:
                        sIndex = p
            except:
                pass

        # if no acceptable start is found return -1

        if sIndex == -1:
            return -1

        if sIndex + 1 >= len(pList):
            return -1

        # print(sIndex, pList[sIndex], pList[sIndex+1])

        if (pList[sIndex] < 4 or pList[sIndex] > 11):
            return -1

        if (pList[sIndex + 1] < 2 or pList[sIndex + 1] > 6):
            return -1

        """ pulses are made up of 2 parts, a fixed length low (approx 0.5-0.6ms)
        and a variable length high.  The length of the high determines whether or
        not a 0,1 or control pulse/bit is being sent.  Highes of length approx 0.5-0.6ms
        indicate a 0, and length of approx 1.6-1.7 ms indicate a 1"""

        for i in range(sIndex + 2, len(pList), 2):
            if i + 1 < len(pList):
                if pList[i + 1] < 0.9:
                    bitList.append(0)
                elif pList[i + 1] < 2.5:
                    bitList.append(1)
                elif (pList[i + 1] > 2.5 and pList[i + 1] < 45):
                    # print('end of data found')
                    break
                else:
                    break

        if self.verbose == True:
            print(bitList)

        # convert the list of 1s and 0s into a
        # binary number

        pulse = 0
        bitShift = 0

        for b in bitList:
            pulse = (pulse << bitShift) + b
            bitShift = 1

        return pulse

    def set_callback(self, callback=None):
        """set_callback, function to allow the user to set
        or change the callback function used at any time"""

        self.callback = callback

        return

    def remove_callback(self):
        """remove_callback, function to allow the user to remove
        the callback function used at any time"""

        self.callback = None

        return

    def print_ir_code(self, code):
        """print_ir_code, function to display IR code received"""

        print(hex(code))

        return

    def set_verbose(self, verbose=True):
        """set_verbose, function to turn verbose mode
        on or off. Used to print out pulse width list
        and bit list"""

        self.verbose = verbose

        return

