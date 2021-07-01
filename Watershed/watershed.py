# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 16:14:18 2020

@author: Mayara
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

filename = "mineral.jpg"
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


#aplicando o watershed
image = segmented_image
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel = np.ones((2,2),np.uint8)

#sure background
closing = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel, iterations = 2)
sure_bg = cv2.dilate(closing,kernel,iterations=3)
dist_transform = cv2.distanceTransform(sure_bg,cv2.DIST_L2,3)

#sure foreground
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
ret, sure_fg = cv2.threshold(dist_transform,0.17*dist_transform.max(),255,0)
sure_fg = np.uint8(sure_fg) 
unknown = cv2.subtract(sure_bg,sure_fg)

ret, segmented_image = cv2.connectedComponents(sure_fg) #marker labelling

segmented_image = segmented_image+1 #background is 1
segmented_image[unknown==255] = 0 #unknown is zero

segmented_image = cv2.watershed(image,segmented_image)

image[segmented_image == -1] = [255,0,0]

plt.imshow(thresh)


filename2 = "coins_watershed_kmeans.jpg"
cv2.imwrite(filename2,image)

"""
#Plot de cada etapa
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(523),plt.imshow(thresh, 'gray')
plt.title("Closing"), plt.xticks([]), plt.yticks([])
plt.subplot(525),plt.imshow(opening, 'gray')
plt.title("Opening"), plt.xticks([]), plt.yticks([])
plt.subplot(526),plt.imshow(sure_bg, 'gray')
plt.title("Dilation"), plt.xticks([]), plt.yticks([])
plt.subplot(527),plt.imshow(dist_transform, 'gray')
plt.title("Distance Transform"), plt.xticks([]), plt.yticks([])
plt.subplot(528),plt.imshow(sure_fg, 'gray')
plt.title("Thresholding"), plt.xticks([]), plt.yticks([])
plt.subplot(529),plt.imshow(unknown, 'gray')
plt.title("Unknown"), plt.xticks([]), plt.yticks([])
plt.subplot(5,2,10),plt.imshow(image, 'gray')
plt.title("Result from Watershed"), plt.xticks([]), plt.yticks([])
"""

