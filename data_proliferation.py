import cv2
import numpy as np
import h5py

#rotation
img = cv2.imread("pp_test.png",0)
height,width = img.shape
M = cv2.getRotationMatrix2D((height/2,width/2),20,1)
dst1= cv2.warpAffine(img,M,(height,width),borderValue=255)
cv2.imwrite("test_rotate.png",dst1)

#affine transformation
pts1 = np.float32([[10,10],[20,10],[10,20]])
pts2 = np.float32([[8,10],[20,10],[10,20]])
M = cv2.getAffineTransform(pts1,pts2)
dst2 = cv2.warpAffine(img,M,(height,width),borderValue=255)
cv2.imwrite("test_affine.png",dst2)

np.savez('data.npz',dst1=dst1,dst2=dst2)
# to retrieve:
# data = np.load('data.npz')
# dst1 = data['dst1']
# dst2 = data['dst2']
