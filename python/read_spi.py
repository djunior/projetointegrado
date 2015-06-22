import spidev

adc = spidev.SpiDev()
adc.open(0,0)

def read(adcnum):
	input = adc.xfer2([1,8 + adcnum << 4,0])
	adcout = ((input[1] & 3) << 8) + input[2]
	return adcout

def read_3201():
	input = adc.xfer([0x00,0x00])
	adcout = (input[1] >> 1) + (input[0]  * (2 ** 7))
	return adcout

def convert_float(v):
	return float(v * (3.3/1023))

def convert_float12bit(v):
	return (float(v)/4096)*3.3

if __name__ == "__main__":

	rawdata = read_3201()
	print "Raw read: " + str(rawdata)
	fvalue = convert_float12bit(rawdata)
	print "Float data: " + str(fvalue)


#	rawdata = read(0)
#	print "Raw read: " + str(rawdata)
#
#	int_value = convert_float(rawdata)
#
#	print "Int value: " + str(int_value)
