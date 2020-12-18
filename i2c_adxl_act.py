import smbus
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

bus = smbus.SMBus(1)

bus.write_byte_data(0x53,0x31,0x2B) #initial data format and fall edge interrupt
bus.write_byte_data(0x53,0x24,0xAA) #set ACT THREHOLD
bus.write_byte_data(0x53,0x25,0x10) #set INACT THREHOLD
bus.write_byte_data(0x53,0x26,0x01)
bus.write_byte_data(0x53,0x27,0x66) #set ACT_x ACT_y INACT_x INACT_y
bus.write_byte_data(0x53,0x2F,0x10) #set INT2 pin receive ACT interrupt
bus.write_byte_data(0x53,0x2E,0x18) #enable ACT INACT interrupt
bus.write_byte_data(0x53,0x2D,0x08) #start measure

def my_callback(channel):
    print('ACT detected')

GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback, bouncetime=300)

while True:
    inter = bus.read_byte_data(0x53,0x30)
    #print('inter = {}'.format(inter))
    sleep(1)
    #if((inter&0x10)==0x10):
    #    print("ACT detected\n")
    #if((inter&0x08)==0x08):
    #    print("INACT detected\n")