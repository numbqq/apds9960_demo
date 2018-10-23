from apds9960.const import *
from apds9960 import APDS9960
import smbus
from time import sleep

port = 8
bus = smbus.SMBus(port)

apds = APDS9960(bus)

try:
    print("Color Sensor Test")
    print("=================")
    apds.enableLightSensor()
    while True:
        sleep(0.25)
        val_a = apds.readAmbientLight()
        val_r = apds.readRedLight()
        val_g = apds.readGreenLight()
        val_b = apds.readBlueLight()
        print "Ambient: {}".format(val_a),
        print "Red: {}".format(val_r),
        print "Green: {}".format(val_g),
        print "Blue: {}".format(val_b)

finally:
    print "Bye"
