import numpy as np
import cv2

class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

def getDif(img,currPoint,tmpPoint):
    return abs(int(img[currPoint.x,currPoint.y]) - int(img[tmpPoint.x,tmpPoint.y]))

def regionGrowing(img,seeds,tol,p = 1):

    height, weight = img.shape
    binaryImg = np.zeros(img.shape)
    seedsLocal = []

    for x in seeds:
        seedsLocal.append(x)
    label = 30
    adj = [Point(-1, -1), Point(0, -1), Point(1, -1), Point(1, 0), \
           Point(1, 1), Point(0, 1), Point(-1, 1), Point(-1, 0)]

    while(len(seedsLocal)>0):
        currPoint = seedsLocal.pop(0); 
        binaryImg[currPoint.x,currPoint.y] = label 
        for i in range(8): 
            tmpX = currPoint.x + adj[i].x 
            tmpY = currPoint.y + adj[i].y
            if tmpX < 0 or tmpY < 0 or tmpX >= height or tmpY >= weight:
                continue
            dif = getDif(img,currPoint,Point(tmpX,tmpY))
            if dif < tol and binaryImg[tmpX,tmpY] == 0: 
                binaryImg[tmpX,tmpY] = label 
                seedsLocal.append(Point(tmpX,tmpY)) 

    return binaryImg

img = cv2.imread('coins.jpg',0)
tol = 10
seeds = [Point(10,10),Point(200,30)]
binaryImg = regionGrowing(img,seeds,tol)

cv2.imwrite('result1.png',binaryImg)

cv2.imshow('input',img)
cv2.imshow('output',binaryImg)
cv2.waitKey(0)


