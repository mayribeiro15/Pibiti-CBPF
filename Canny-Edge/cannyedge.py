# -*- coding: utf-8 -*-
"""
Created on Wed May 12 23:47:24 2021

@author: Mayara
"""
import numpy as np
import cv2

filename = "idaho.jpg"
image = cv2.imread(filename) #lendo a imagem

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

#aplicando o filtro gaussiano
cv2.imshow("Original", image)

canny_image = cv2.Canny(blurred, 30, 150) #tight 240,250 / mid 30,150 / wide 10,200
image[canny_image != 0] = [0,255,0]

cv2.imshow("Canny Edge", image)
cv2.waitKey(0)

filename2 = "idaho_cannyedge_kmeans.jpg"
cv2.imwrite(filename2,image)


