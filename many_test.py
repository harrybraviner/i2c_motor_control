#! /usr/bin/python

from smbus import SMBus
from time import sleep

MOTOR_CONTROLLER_ADDR = 0x0a;

LEFT_FORE = 0b00000001
LEFT_BACK = 0b00000010
LEFT_STOP = 0b00000000
RIGHT_FORE = 0b00000100
RIGHT_BACK = 0b00001000
RIGHT_STOP = 0b00000000

SET_DIR_SPEED_CMD = 0x01

def set_speeds(left_speed, right_speed):
	# Enforce limits due to 8-bit resolution
	if(left_speed < -0xff):		left_speed = -0xff
	if(left_speed > +0xff):		left_speed = +0xff
	# Enforce limits due to 8-bit resolution
	if(right_speed < -0xff):	right_speed = -0xff
	if(right_speed > +0xff):	right_speed = +0xff

	direction = 0x00;
	if(left_speed < 0):		direction |= LEFT_BACK
	elif(left_speed > 0):	direction |= LEFT_FORE
	if(right_speed < 0):		direction |= RIGHT_BACK
	elif(right_speed > 0):	direction |= RIGHT_FORE

	bus.write_i2c_block_data(MOTOR_CONTROLLER_ADDR, SET_DIR_SPEED_CMD, [direction, abs(left_speed), abs(right_speed)])


# Begin setup
bus = SMBus(1)
# End setup

dataBlock = [0b00001001, 0x2f, 0x0f]

#bus.write_byte_data(0xa, 0x3f, 0xaa)
#bus.write_i2c_block_data(0xa, 0x01, dataBlock)
#set_speeds(0xd0, 0x00)
#set_speeds(0xff, 0xff)
#set_speeds(0xff, 0xff)
#sleep(1)
#set_speeds(0x00, 0x00)
for i in range(100):
	try:
		set_speeds(i, i)
	except IOError:
		print "IOError at i = ", i
