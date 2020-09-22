import cv2
import imutils
import Main 
#from centroidtracker import CentroidTracker

vehicle_cascade = cv2.CascadeClassifier('casDATABARU.xml')

video_path = 'Set01_video01.h264'
cap = cv2.VideoCapture(video_path)
#ct = CentroidTracker()
# cv2.resizeWindow("ssss", 300, 300)
while True:
	#(_, img) = webcam.read() 
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	vehicles = vehicle_cascade.detectMultiScale(gray, 1.3, 4)
	#rects = []
	#list_rects = []
	for (x, y, w, h) in vehicles:
		startX = x
		startY = y
		endX = (w + x)
		endY = (h + y)
		#list_rects.append((startX, startY, endX, endY))
		img = cv2.rectangle(img, (startX, startY), (endX, endY), (0, 255, 0), 2)
		croped = img[startY:endY, startX:endX]
		plat = Main.main(croped)
		cv2.waitKey(1)


	#cv2.line(img, (200,140), (300,140), (0, 0, 255), 2)
	#cv2.line(img, (80,180), (240,180), (0, 0, 255), 2)
	#cv2.putText(img, 'ROI-in', (520,25), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 2, cv2.LINE_AA) 
	#cv2.line(img, (0,225), (460,225), (0, 0, 255), 2)
	#cv2.putText(img, 'ROI-out', (480,230), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 2, cv2.LINE_AA) 
	# cropGray = cv2.cvtColor(croped,1)
	imgRe = imutils.resize(img, width=720)
	# cv2.imwrite('CROPP.png', croped)
	cv2.imshow('OpenCV', imgRe)
        #cv2.resizeWindow("frame", 800,600)
	# plat = Main.main(img)
	

	# if cv2.waitKey(1) & 0xFF == ord("a"):
	# 	plat = Main.main(croped)

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

# plat = Main.main(croped)

cap.release()
cv2.destroyAllWindows()
