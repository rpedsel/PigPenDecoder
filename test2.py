import numpy as np
import cv2
import matplotlib.pyplot as plt 

class Rect:
    def __init__(

img = cv2.imread('pp.png')
#mser = cv2.MSER_create()
h_img, w_img,_ = img.shape
size = h_img*w_img
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Converting to GrayScale
vis = img.copy()
ret,thresh = cv2.threshold(gray,127,255,0)
_,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#cnt = contours[0]
#M = cv2.moments(cnt)
#print(M)
cv2.drawContours(vis, contours, -1, (0,255,0), 1)

#check = {}
#regions,_ = mser.detectRegions(gray)
#hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
#for p in hulls:
#    x,y,w,h = cv2.boundingRect(p)
#    if (x,y) not in check.keys():
#        cv2.rectangle(vis,(x,y),(x+w,y+h),(0,255,0),1)
#        check[(x,y)] = True
#        print(p)
#        print("new:")
#hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
#print(len(hulls))
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    if w*h < size/2:
        cv2.rectangle(vis,(x,y),(x+w,y+h),(0,0,255),1)

#cv2.polylines(vis, hulls, 1, (0, 0, 255), 1)
cv2.imwrite('output.jpg', vis)
