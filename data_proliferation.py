import cv2
import numpy as np

#rotation
img = cv2.imread("pp_test.png",0)
height,width = img.shape
M = cv2.getRotationMatrix2D((height/2,width/2),20,1)
dst= cv2.warpAffine(img,M,(height,width),borderValue=255)
cv2.imwrite("test.jpg",dst)



