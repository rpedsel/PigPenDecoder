import numpy as np
import cv2
from itertools import combinations

class Rect:
    def __init__(self, x,y,w,h):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.area = h*w
        self.marked = False
    def mark(self):
        self.marked = True
    def ismarked(self):
        return self.marked

def if_intersect(rect1, rect2):
    x = max(rect1.x, rect2.x)
    y = max(rect1.y, rect2.y)
    w = min(rect1.x + rect1.w, rect2.x + rect2.w) - x
    h = min(rect1.y + rect1.h, rect2.y + rect2.h) - y
    if w<0 or h<0:
        return False
    return True

def union(rect1, rect2):
    x = min(rect1.x, rect2.x)
    y = min(rect1.y, rect2.y)
    w = max(rect1.x + rect1.w, rect2.x + rect2.w) - x
    h = max(rect1.y + rect1.h, rect2.y + rect2.h) - y
    return Rect(x, y, w, h)

def process(img_file):
    img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
    h_img, w_img = img.shape
    size = h_img*w_img
    
    vis = img.copy()
    _,thresh = cv2.threshold(img,127,255,0)
    _,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    rectList = []
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        if w*h < size-20 and w*h > 20:   
            rectList.append(Rect(x,y,w,h))

    count = 3
    while(count > 0):
        rectComb = combinations(rectList,2)
        resRect = []
        for comb in rectComb:
            if if_intersect(comb[0],comb[1]):
                resRect.append(union(comb[0],comb[1]))
                comb[0].mark()
                comb[1].mark()
        resRect += [r for r in rectList if not r.ismarked()]
        count -= 1
        rectList = resRect
    
    data = []
    for r in resRect:
        cv2.rectangle(vis,(r.x,r.y),(r.x+r.w,r.y+r.h),(0,0,255),1)
        maxwh, maxw = max(r.w,r.h), r.w > r.h 
        crop = cv2.resize(img[r.y:r.y+r.h,r.x:r.x+r.w],(0,0),fx=20/maxwh, fy=20/maxwh)
        (_, crop) = cv2.threshold(crop, 128,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        crop = 1-crop/255
        mat = np.zeros((28,28))
        if maxw:
            starty = int(np.ceil((28-crop.shape[0])/2))
            mat[starty:starty+crop.shape[0], 4:4+crop.shape[1]] = crop
        else:
            startx = int(np.ceil((28-crop.shape[1])/2))
            mat[4:4+crop.shape[0], startx:startx+crop.shape[1]] = crop
        data.append((mat.reshape(-1), (r.x, r.y, r.w, r.h)))
    cv2.imwrite("output.jpg", vis)
    return data

