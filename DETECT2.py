import numpy as np
import cv2
import Main

car_cascade = cv2.CascadeClassifier('cascade.xml')

img = cv2.imread('102.png')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img,0)
resized=cv2.resize(gray,(int(gray.shape[1]/2),int(gray.shape[0]/2)))
cars=car_cascade.detectMultiScale(gray)
# # img_croped = []
for (x,y,w,h) in cars:
    img = cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
    # img_croped.append(gray[y:y+h, x:x+w])
    croped = img[y:y+h, x:x+w]
# for croped in img_croped:
#     # cv2.imshow('Crop', croped)
#     cv2.waitKey(0)
# resized=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
# crop_copy = croped.copy()
cv2.imshow('DETECT',img)
# cv2.imshow('Crop', croped)
cv2.imwrite('crop.png', croped)
# print(croped.dtype)
cropGray = cv2.cvtColor(croped,1)
# print(cropGray.shape)
# cv2.imshow('cropGray', cropGray)
# crop2 = np.array(crop_copy)
plat_nomor = Main.main(cropGray)
# print(plat_nomor)
cv2.waitKey(0)
cv2.destroyAllWindows()
