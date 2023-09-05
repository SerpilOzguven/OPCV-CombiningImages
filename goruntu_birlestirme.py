import cv2
import numpy as np


#resmi içe aktar

image = cv2.imread("lenna.png")
cv2.imshow("Original", image)


hor = np.hstack((image,image))
cv2.imshow("Yatay", hor)     


#dikey
ver = np.vstack((image,image)) 
cv2.imshow("Dikey", ver)

          