from RPi import GPIO
from time import sleep
import tm1637
tm = tm1637.TM1637(clk=5, dio=4)

clk = 17
dt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)
tm.write([0b00000000, 0b10000000, 0b00001111, 0b00000000])

try:

        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 0.5
                        else:
                                counter -= 0.5
                                if counter < 1:
                                    counter = 1
                        print(counter, "🎉")
                        tm.number(int(counter))
                        file = open("/home/master/eksamensprojekt/nummer.txt", "w")
                        file.write(str(int(counter)))
                        file.close()
                clkLastState = clkState
finally:
        GPIO.cleanup()