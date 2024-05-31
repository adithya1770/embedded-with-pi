from mq2 import MQ2
from machine import Pin, PWM
import utime
from time import sleep
MID = 1500000
MIN = 1000000
MAX = 2000000
pwm = PWM(Pin(4))
pwm.freq(50)
pwm.duty_ns(MID)
pin=26
sensor = MQ2(pinData = pin, baseVoltage = 3.3)
print("Calibrating")
sensor.calibrate()
print("Calibration completed")
print("Base resistance:{0}".format(sensor._ro))
led = Pin(7, Pin.OUT)
while True:
    print(sensor.readSmoke())
    if (sensor.readSmoke())>125:
        led.on()
        sleep(2)
        led.off()
        pwm.duty_ns(MIN)
        sleep(1)
        pwm.duty_ns(MAX)
        sleep(1)
        break
    else:
        continue
