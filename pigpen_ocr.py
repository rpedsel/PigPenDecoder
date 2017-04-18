import text_rec
import mnist
from sys import argv
import numpy as np

import cv2

data = text_rec.process(argv[1])
data_image = np.array(list(map(lambda x: x[0],data)))
p = mnist.cnn(data_image)

#print(np.array(list(map(int,(data[-3][0])))).reshape(28,28))

pos = list(map(lambda x: x[1],data))
img = cv2.imread(argv[1]).copy()
font = cv2.FONT_HERSHEY_SIMPLEX

for i in range(len(p)):
    cv2.putText(img,str(p[i]),(pos[i][0],pos[i][1]+15), font,0.8,(0,0.5,255),1)

cv2.imwrite("puttext.jpg",img)
