import cv2
import numpy as np
import math

def PSNR(HR, LR):
    MSE = np.mean((HR - LR) ** 2)
    result = 20 * math.log10((255/np.sqrt(MSE)))
    return result

img = cv2.imread('', cv2.IMREAD_GRAYSCALE)
img_LR1 = cv2.resize(img, (10, 10))
img_LR1 = cv2.resize(img_LR1, (440, 440))
print("psnr : ", PSNR(img, img_LR1))

