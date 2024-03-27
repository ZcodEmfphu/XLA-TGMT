import numpy as np
import cv2 as cv

file ='D:\Project\XLA-TGMT\week1\img\sunflower.jpg'
img = cv.imread(file)

# cv.imshow('Original', img)
cv.waitKey(0)

print(f'Original shape: {img.shape}')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY);
print(f'Gray shape: {gray.shape}')

cv.imshow('Original', img)
cv.waitKey(0)