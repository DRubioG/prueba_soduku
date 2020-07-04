import cv2
import numpy as np

thres=240

imgR=cv2.imread('test.png', 0)
img=cv2.resize(imgR, (300,300), interpolation=cv2.INTER_LINEAR)

height, width = img.shape[:2]
#print(height)
#print(width)

#
ret, imgthres=cv2.threshold(img, thres, 255, cv2.THRESH_BINARY)

cv2.rectangle(imgthres, (1,1), (width-1, height-1), (255, 255, 255), 3)

contours,hierarchy =cv2.findContours(imgthres, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#print((contours))
areas=[]
anchos=[]
i=0
numero=[]
num=[]
for con in contours:
    area=cv2.contourArea(con)
    if (area > 200) & (area< 2000):
        x,y, h, w=cv2.boundingRect(con)
        #cv2.rectangle(img, (x+4,y+4), (x+w-4, y+h-4), (255, 0, 0), 1)
        areas.append(con)
        pru=imgthres[y+4:y+h-4, x+4:x+w-4]
        
        media=cv2.mean(pru)[0]
        if  media < 254.9:
          #print("dentro")
          #numero.append(con)
          #pru2=cv2.resize(pru, (300,300), interpolation=cv2.INTER_LINEAR)
          cv2.rectangle(pru, (1,1), (h-4, w-4), (255, 255, 255), 2)
          
          conN, hierN=cv2.findContours(pru, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
          pru=cv2.cvtColor(pru, cv2.COLOR_GRAY2BGR)
          cv2.drawContours(pru, conN, -1, (0,200,0))
          cv2.imshow("pru", pru)
          cv2.waitKey(0)
          #num.append(conN)
          for cont in conN:
            #num.append(cont)
            #print(cont[0])
           # imgH=cv2.resize(img, (300*w,300*h), interpolation=cv2.INTER_LINEAR)
            cv2.drawContours(img, cont+[x+4, y+4], -1, (255, 255,0), 1, 1)
            #
          
          #cv2.drawContours(img, conN, i, (0,255,0), 1)
           # i=i+1
#for i in range(len(conN)):
#print(len(num))
imgthres=cv2.cvtColor(imgthres, cv2.COLOR_GRAY2BGR)
#cv2.drawContours(img, numero, -1, (0, 0,255), 1)
cv2.drawContours(imgthres, contours, -1, (255, 0,0))
imgH=cv2.resize(img, (300,300), interpolation=cv2.INTER_LINEAR)
cv2.imshow("img", imgH)
cv2.imshow("threshold", imgthres)
cv2.waitKey(0)
