import numpy as np
import math
import cv2
import cv

def create(array,width = 500,height = 300):
	img =  np.zeros((height,width,3),np.uint8)

	fontFace = cv.CV_FONT_HERSHEY_SIMPLEX
	fontSize = 0.6
	fontColor = (255,255,255)
	
	workWidth = int(width*0.8)
	workHeight = int(height*0.8)
	
	startX = int(width*0.1)
	startY = int(height*0.1)

	# Vertical line
	cv2.line(img,(startX,startY),(startX,startY + workHeight),(255,255,255),1)

	# Horizontal line
	cv2.line(img,(startX,startY+workHeight),(startX+workWidth,startY+workHeight),(255,255,255),1)

	if (len(array) <= 0):
		return img
	
	indexStr = str(0)
	indexStrSize,baseline = cv2.getTextSize(indexStr,fontFace,fontSize,1)
	cv2.putText(img,indexStr,(startX,startY+workHeight+indexStrSize[1]+(startY - indexStrSize[1])/2),fontFace,fontSize,fontColor)

	indexStr = "{0:.2f}".format(min(array))
	indexStrSize,baseline = cv2.getTextSize(indexStr,fontFace,fontSize,1)
	cv2.putText(img,indexStr,(startX-indexStrSize[0],startY+workHeight),fontFace,fontSize,fontColor)

	steps = workWidth / (len(array)-1)
	resolution = workHeight / (max(array) - min(array))
	offset = (-1)*min(array) * resolution
	print "Steps: " + str(steps)
	print "Resolution: " + str(resolution)

	for index in range(0,len(array)-1):	
		x1 = int(startX + index*steps)
		y1 = startY+ workHeight - int((array[index]*resolution + offset))
		x2 = int(startX + (index+1)*steps)
		y2 = startY+ workHeight - int((array[index+1]*resolution + offset))
		print "(x,y) = (" + str(x1) + "," + str(y1) + "), to (x,y) = (" + str(x2) + "," + str(y2) + ")"
		cv2.line(img,(x1,y1),(x2,y2),(255,0,0),5)

		indexStr = str(index+1)
		indexStrSize,baseline = cv2.getTextSize(indexStr,fontFace,fontSize,1)
		cv2.putText(img,indexStr,(x2,startY+workHeight+indexStrSize[1]+(startY - indexStrSize[1])/2),fontFace,fontSize,fontColor)

	return img

if __name__ == '__main__':
	l = [0,1,0,2,2,1,2,1,4,5,3,2,0,0,0,0,1]
	img = create(l)

	cv2.imshow("window",img)
	cv2.waitKey(0)

