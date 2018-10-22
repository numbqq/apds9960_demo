from apds9960.const import *
from apds9960 import APDS9960
import smbus
from time import sleep

port = 8
bus = smbus.SMBus(port)

apds = APDS9960(bus)

def intH(channel):
    print("INTERRUPT")

try:
    apds.setProximityIntLowThreshold(50)

    print("Proximity Sensor Test")
    print("=====================")
    apds.enableProximitySensor()
    oval = -1
    while True:
        sleep(0.25)
        val = apds.readProximity()
        if val != oval:
            print("proximity={}".format(val))
            oval = val

finally:
    print "Bye"
