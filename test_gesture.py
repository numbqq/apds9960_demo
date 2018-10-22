from apds9960.const import *
from apds9960 import APDS9960
import smbus
from time import sleep

port = 8
bus = smbus.SMBus(port)

apds = APDS9960(bus)

def intH(channel):
    print("INTERRUPT")

dirs = {
    APDS9960_DIR_NONE: "none",
    APDS9960_DIR_LEFT: "left",
    APDS9960_DIR_RIGHT: "right",
    APDS9960_DIR_UP: "up",
    APDS9960_DIR_DOWN: "down",
    APDS9960_DIR_NEAR: "near",
    APDS9960_DIR_FAR: "far",
}
try:

    apds.setProximityIntLowThreshold(50)

    apds._write_byte_data(APDS9960_REG_GOFFSET_U, 30)
    apds._write_byte_data(APDS9960_REG_GOFFSET_D, 30)
    apds._write_byte_data(APDS9960_REG_GOFFSET_L, 30)
    apds._write_byte_data(APDS9960_REG_GOFFSET_R, 30)


    print("Gesture Test")
    print("============")
    apds.enableGestureSensor()
    while True:
        sleep(0.5)
        if apds.isGestureAvailable():
            motion = apds.readGesture()
            print("Gesture={}".format(dirs.get(motion, "unknown")))


finally:
    print "Bye"
