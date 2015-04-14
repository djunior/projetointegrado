import cv
import cv2
import sys
import numpy

version = sys.version
if version[0] == "3":
    import statistics
else:
	def mean(list):
	    sum = 0
	    for element in list:
	        sum += element
	    return sum/len(list)

	def variance(list):
		var = 0
		for element1 in list:
			for element2 in list:
				var += ((element1 - element2) ** 2)/2
		return var/(len(list)**2)

img1 = cv2.imread("images/wave_1.png",cv2.IMREAD_COLOR)
img2 = cv2.imread("images/wave_2.png",cv2.IMREAD_COLOR)
img3 = cv2.imread("images/wave_3.png",cv2.IMREAD_COLOR)
img4 = cv2.imread("images/wave_4.png",cv2.IMREAD_COLOR)
img5 = cv2.imread("images/wave_5.png",cv2.IMREAD_COLOR)

img1 = cv2.cvtColor(img1,cv.CV_BGR2HSV)
img2 = cv2.cvtColor(img2,cv.CV_BGR2HSV)
img3 = cv2.cvtColor(img3,cv.CV_BGR2HSV)
img4 = cv2.cvtColor(img4,cv.CV_BGR2HSV)
img5 = cv2.cvtColor(img5,cv.CV_BGR2HSV)

def histogram(img):
	channels = [0]
	mask = None
	histSize = [256]
	ranges = [0,255]
	return cv2.calcHist([img], channels, mask, histSize, ranges)

def gradient(img):
	img = cv2.GaussianBlur( img, (3,3), 0 );
	sobel = cv2.Sobel(img,cv2.CV_64F,1,1,ksize=3)
	#sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
	return sobel

hist1 = histogram(img1)
hist2 = histogram(img2)
hist3 = histogram(img3)
hist4 = histogram(img4)
hist5 = histogram(img5)

diff12 = cv2.compareHist(hist1,hist2,0)
diff13 = cv2.compareHist(hist1,hist3,0)
diff14 = cv2.compareHist(hist1,hist4,0)
diff15 = cv2.compareHist(hist1,hist5,0)

print "Correlation 1 2: " + str(diff12)
print "Correlation 1 3: " + str(diff13)
print "Correlation 1 4: " + str(diff14)
print "Correlation 1 5: " + str(diff15)

list = [diff12,diff13,diff14,diff15]

print "Mean: " + str(mean(list))
print "Variance: " + str(variance(list))

img_grey = cv2.imread("images/wave_1.png",2)
grad = gradient(img_grey)

img_grey2 = cv2.imread("images/wave_2.png",2)
grad2 = gradient(img_grey2)

img_grey3 = cv2.imread("images/wave_3.png",2)
grad3 = gradient(img_grey3)

img_grey4 = cv2.imread("images/wave_4.png",2)
grad4 = gradient(img_grey4)

img_grey5 = cv2.imread("images/wave_5.png",2)
grad5 = gradient(img_grey5)

def stat(g):
	return (numpy.mean(g),numpy.std(g),numpy.var(g))

def diff_stat(g1,g2):
	diff = g2 - g1
	return stat(diff)

print "Mean 			STD 			VAR"
print stat(grad)
print stat(grad2)
print stat(grad3)
print stat(grad4)
print stat(grad5)


print "Mean 			STD 			VAR"
print str(diff_stat(grad,grad2))
print str(diff_stat(grad2,grad3))
print str(diff_stat(grad3,grad4))
print str(diff_stat(grad4,grad5))

# cv2.imshow("image1",std)
# cv2.imshow("image2",grad3)
# cv2.imshow("image diff",grad_diff)
# cv2.imshow("image inverse",grad_inverse)
# cv2.waitKey(0)

# cv2.destroyAllWindows()
