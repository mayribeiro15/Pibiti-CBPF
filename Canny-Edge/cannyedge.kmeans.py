# -*- coding: utf-8 -*-
"""
Created on Wed May 12 23:47:24 2021

@author: Mayara
"""
import numpy as np
import cv2

filename = "idaho.jpg"
image = cv2.imread(filename) #lendo a imagem

#aplicando o k-means
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #convertendo para RGB
pixel_values = image.reshape((-1, 3)) #imagempara 2D e 3 cores
pixel_values = np.float32(pixel_values) #converter para float
print(pixel_values.shape)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
flags = cv2.KMEANS_RANDOM_CENTERS

k = 2
compactness, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, flags)

centers = np.uint8(centers) # convert back to 8 bit values
labels = labels.flatten() # flatten the labels array?
segmented_image = centers[labels.flatten()] #converter cores = centroide
segmented_image = segmented_image.reshape(image.shape) #reshape para imagem original

image = segmented_image

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

#aplicando o filtro gaussiano
cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)

canny_image = cv2.Canny(blurred, 30, 150) #tight 240,250 / mid 30,150 / wide 10,200

cv2.imshow("Canny Edge Map", canny_image)
cv2.waitKey(0)

filename2 = "idaho_cannyedge_kmeans.jpg"
cv2.imwrite(filename2,canny_image)


