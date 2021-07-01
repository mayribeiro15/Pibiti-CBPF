# -*- coding: utf-8 -*-
"""
Created on Thu Jun  10 11:11:30 2021

@author: Mayara
"""

from skimage.exposure import rescale_intensity
import numpy as np
import cv2

#Funcao de convolucao a ser aplicada nos filtros
def convolve(image, K):
	(iH, iW) = image.shape[:2]
	(kH, kW) = K.shape[:2]
	pad = (kW - 1) // 2
	image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
		cv2.BORDER_REPLICATE)
	output = np.zeros((iH, iW), dtype="float")

	for y in np.arange(pad, iH + pad):
		for x in np.arange(pad, iW + pad):
			roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
			k = (roi * K).sum()
			output[y - pad, x - pad] = k

	output = rescale_intensity(output, in_range=(0, 255))
	output = (output * 255).astype("uint8")
	return output



image = cv2.imread("idaho.jpg") #lendo a imagem
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convertendo para grayscale

# Filtos hard-coded
smallBlur = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))
largeBlur = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))
sharpen = np.array((
	[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]), dtype="int")
laplacian = np.array((
	[0, 1, 0],
	[1, -4, 1],
	[0, 1, 0]), dtype="int")
sobelX = np.array((
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]), dtype="int")

sobelY = np.array((
	[-1, -2, -1],
	[0, 0, 0],
	[1, 2, 1]), dtype="int")
emboss = np.array((
	[-2, -1, 0],
	[-1, 1, 1],
	[0, 1, 2]), dtype="int")

#Banco com todos os filtros
kernelBank = (
	#("small_blur", smallBlur),
	#("large_blur", largeBlur),
	#("sharpen", sharpen),
	("laplacian", laplacian),
	#("sobel_x", sobelX),
	#("sobel_y", sobelY),
	#("emboss", emboss)
    )

for (kernelName, K) in kernelBank:
	print("[INFO] applying {} kernel".format(kernelName))
	convolveOutput = convolve(gray, K)
	opencvOutput = cv2.filter2D(gray, -1, K)
	cv2.imshow("Original", gray)
	cv2.imshow("{} - convole".format(kernelName), convolveOutput)
	cv2.imshow("{} - opencv".format(kernelName), opencvOutput)
    

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("idaho_opencv.jpg",opencvOutput)
cv2.imwrite("idaho_convolve.jpg",convolveOutput)
