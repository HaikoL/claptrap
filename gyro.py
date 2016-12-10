#!/usr/bin/python

import smbus
import math


power_mgmt_1 = 0x6b
address = 0x68


def read_word(reg):
	h = bus.read_byte_data(address, reg)
	l = bus.read_byte_data(address, reg+1)
	value = (h << 8) + l
	return value

def read_word_2c(reg):
	val = read_word(reg)

	if (val >= 0x8000):
		return -((65535 - val) + 1)
	else:
		return val

def dist(a, b):
	return math.sqrt((a*a) + (b*b))

def get_y_rotation(x, y, z):
	radians = math.atan2(x, dist(y,z))
	return -math.degrees(radians)

def get_x_rotation(x, y, z):
	radians = math.atan2(y, dist(x,z))
	return math.degrees(radians)


bus = smbus.SMBus(1) 
bus.write_byte_data(address, power_mgmt_1, 0)
	


bes_x = read_word_2c(0x3b)
bes_y = read_word_2c(0x3d)
bes_z = read_word_2c(0x3f)
	
bs_x = bes_x / 16384.0
bs_y = bes_y / 16384.0
bs_z = bes_z / 16384.0

rotation_x = get_x_rotation(bs_x, bs_y, bs_z)
rotation_y = get_y_rotation(bs_x, bs_y, bs_z)


print "X-Rotation: " + str(rotation_x)
print "Y-Rotation: " + str(rotation_y)
