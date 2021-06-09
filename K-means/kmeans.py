# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:23:06 2020

Primeiro exemplo de K-Means

@author: Mayara
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

filename = "graocolor.jpg"
image = cv2.imread(filename) #lendo a imagem
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #convertendo para RGB
pixel_values = image.reshape((-1, 3)) #imagempara 2D e 3 cores
pixel_values = np.float32(pixel_values) #converter para float
print(pixel_values.shape)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

k = 9
_, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

centers = np.uint8(centers) # convert back to 8 bit values
labels = labels.flatten() # flatten the labels array?
segmented_image = centers[labels.flatten()] #converter cores = centroide
segmented_image = segmented_image.reshape(image.shape) #reshape para imagem original

plt.imshow(segmented_image)

filename2 = "graocolor_kmeans.jpg"
cv2.imwrite(filename2,segmented_image)

