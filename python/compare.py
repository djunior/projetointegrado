# IMPORTS
import cv2
import cv
import numpy
import sys
import math

# CONSTANTS
INTERVAL = 2.0
BETA = 0.4
WAVE_VALUES = {'FLAT': [0, 0.2], 'SMALL': [0.2, 0.4], 'MEDIUM': [0.4, 0.7], 'BIG': [0.7, 1.2], 'HUGE': [1.2, 100]}

# RESULTS
WAVE_INTERVAL = 0
WAVE_HEIGHT = 0

# FUNCTIONS

# COMPARE 2 HISTOGRAMS
def compare(x, y):

	img_01 = cv2.imread(x)
	img_02 = cv2.imread(y)

	channels = [0, 1, 2]

	correls = []

	for channel in channels:
		hist_01 = cv2.calcHist([img_01], [channel], None, [256], [0, 256])
		hist_02 = cv2.calcHist([img_02], [channel], None, [256], [0, 256])

		correl = cv2.compareHist(hist_01, hist_02, cv.CV_COMP_CORREL)
		chisqr = cv2.compareHist(hist_01, hist_02, cv.CV_COMP_CHISQR)
		intersect = cv2.compareHist(hist_01, hist_02, cv.CV_COMP_INTERSECT)
		bhattacharyya = cv2.compareHist(hist_01, hist_02, cv.CV_COMP_BHATTACHARYYA)
		
		correls.append(correl)

		'''
		print 'Channel ' + str(channel) 
		print 'Correlation: ' + str(correl)
		print 'Chi-Squared: ' + str(chisqr)
		print 'Intersection: ' + str(intersect)
		print 'Bhattacharrya Distance: ' + str(bhattacharyya)  
		'''

	hist_01 = cv2.calcHist([img_01], [2], None, [256], [0, 256])
	hist_02 = cv2.calcHist([img_02], [2l], None, [256], [0, 256])
	correl = cv2.compareHist(hist_01, hist_02, cv.CV_COMP_CORREL)

#	return correl
	return get_mean(correls)


def get_wave_break(correl_array):
	min_correl = 1
	index = 0 
	for i in range(0, len(correl_array)):
		correl = correl_array[i]
		if correl < min_correl:
			index = i
			min_correl = correl

	return [index, min_correl]


def get_wave_period(correl_array):
	mean = get_mean(correl_array)
	std_deviation = get_std_deviation(correl_array)
	std_error = get_std_error(correl_array)

	wave_breaks = []
	MARGIN = 2

	for i in range(0, len(correl_array)):
		if correl_array[i] < mean - std_deviation:
			if not check_in_margin(wave_breaks, i, MARGIN):
				wave_breaks.append(i)


	if len(wave_breaks) == 1:
		return 0
	else:
		wave_interval =  (wave_breaks[-1] - wave_breaks[0]) / (len(wave_breaks) - 1)
		return wave_interval * INTERVAL


def check_in_margin(list, x, margin):
	if margin == 0:
		return False
	elif math.fabs(x - margin) in list:
		return True
	else:
		return check_in_margin(list, x, margin - 1)

def get_wave_height(correl_array, index):
	x = math.fabs(correl_array[index - 1] - correl_array[index - 2])
	a = 1 / (INTERVAL * BETA)
	
	return a * x

def get_wave_value(h):
	for key in WAVE_VALUES:
		if h > WAVE_VALUES[key][0] and h < WAVE_VALUES[key][1]:
			return key

def get_mean(x):
	sum = 0
	N = len(x)
	for y in x:
		sum += y

	mean = sum / N
	return mean

def get_std_error(x):
	return get_std_deviation(x) / math.sqrt(len(x))

def get_std_deviation(x):
	mean = get_mean(x)
	aux = 0
	for y in x:
		aux += (y - mean) ** 2

	std_deviation = math.sqrt(aux / len(x))
	return std_deviation

def gradient(img):
	return cv2.Sobel(img,cv.CV_64F,1,1,ksize=3)

def stat(grad,hist):
	return (numpy.mean(grad),hist,numpy.std(grad),numpy.var(grad))

def stat_diff(grad1,grad2):
	diff = grad2 - grad1
	return stat(diff)

if __name__ == '__main__':
	waves = sys.argv[1:]
	correl_array = []
	gradient_array = []
	for i in range(1, len(waves)):
		correl = compare(sys.argv[i], sys.argv[i + 1])
		correl_array.append(correl)
		img = cv2.imread(sys.argv[i],2)
		grad = gradient(img)
		gradient_array.append(grad)

	print correl_array
	for g in range(0,len(gradient_array)):
		print stat(gradient_array[g],correl_array[g])
	WAVE_INTERVAL = get_wave_period(correl_array)
	print 'WAVE INTERVAL: ' + str(WAVE_INTERVAL)	

	min = get_wave_break(correl_array)
	print min
	index = min[0]
	WAVE_HEIGHT = get_wave_height(correl_array, index)
	print 'WAVE HEIGHT: ' + str(WAVE_HEIGHT)	
	WAVE_VALUE = get_wave_value(WAVE_HEIGHT)
	print 'WAVE VALUE: ' + WAVE_VALUE
	

