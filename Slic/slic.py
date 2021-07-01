# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:37:45 2020

Primeiro exemplo de SLIC

@author: Mayara
"""

from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
import numpy as np
import matplotlib.pyplot as plt
import cv2 

image = cv2.imread("carb.jpg") #lendo a imagem
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #convertendo para RGB
pixel_values = image.reshape((-1, 3)) #imagempara 2D e 3 cores
pixel_values = np.float32(pixel_values) #converter para float
print(pixel_values.shape)

fig = plt.figure()

segments = slic(image, 20, sigma = 2)

ax = fig.add_subplot(1, 1, 1)
ax.imshow(mark_boundaries(image,segments))
segmented_image = mark_boundaries(image,segments)

plt.show(ax)
