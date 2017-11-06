
# coding: utf-8

# In[11]:



"""
copyright Simin Zhai siminz@bu.edu
"""
import numpy as np
# import skimage
import cv2
import random

def add_gaussian_noise(srcArr,mean,sigma):
    noiseArr = srcArr.copy()
    noiseArr = np.random.normal(mean,sigma,srcArr.shape)
    np.add(srcArr,noiseArr,srcArr,casting="unsafe")
    return srcArr;

def add_salt_pepper_noise(img,pa,pb):
    row,col,h=img.shape
    amount1=row*col*pa
    amount2=row*col*pb
    for i in range(int(amount1)):
        img[int(random.uniform(0,row))][int(random.uniform(0,col))]=0
    for i in range(int(amount2)):
        img[int(random.uniform(0,row))][int(random.uniform(0,col))]=255
        
# --- Gaussian mean = 0 sigma = 20 ;filter kernel size 3*3;S&P 0.01 0.01 for example#        
image=cv2.imread('C:\Users\simin\Desktop\ec601\OpenCV_homework\Test_images\emma.png')
cv2.namedWindow('Original image')
cv2.imshow('Original',image)
cv2.imwrite('Original.png',image)


image_noise=image.copy()
add_gaussian_noise(image_noise,0,20)
cv2.imshow('Gaussian_noise',image_noise)
cv2.imwrite('C:\Users\simin\Desktop\ec601\OpenCV_homework\exercise3\Gaussian_noise.png',image_noise)

image_smoothing1=image_noise.copy()
cv2.blur(image_smoothing1,(3,3))
cv2.imshow('Boxfilter',image_smoothing1)
cv2.imwrite('C:\Users\simin\Desktop\ec601\OpenCV_homework\exercise3\Boxfilter.png',image_smoothing1)

image_smoothing2=image_noise.copy()
cv2.GaussianBlur(image_smoothing2,(3,3),1.5)
cv2.imshow('Gaussian',image_smoothing2)
cv2.imwrite('C:\Users\simin\Desktop\ec601\OpenCV_homework\exercise3\Gaussian.png',image_smoothing2)

image_smoothing3=image_noise.copy()
cv2.medianBlur(image_smoothing3,3)
cv2.imshow('Median',image_smoothing3)
cv2.imwrite('C:\Users\simin\Desktop\ec601\OpenCV_homework\exercise3\Median.png',image_smoothing3)

image_noise2=image.copy()
add_salt_pepper_noise(image_noise2,0.01,0.01)
cv2.imshow("S&P", image_noise2)
cv2.imwrite("C:\Users\simin\Desktop\ec601\OpenCV_homework\exercise3\S&P.png", image_noise2)

image_smoothing4=image_noise2.copy()
cv2.blur(image_smoothing4,(3,3))
cv2.imshow('Boxfilter2',image_smoothing4)
cv2.imwrite('C:\Users\simin\Desktop\ec601\OpenCV_homework\exercise3\Boxfilter2.png',image_smoothing4)

image_smoothing5=image_noise2.copy()
cv2.GaussianBlur(image_smoothing5,(3,3),1.5)
cv2.imshow('Gaussian2',image_smoothing5)
cv2.imwrite('C:\Users\simin\Desktop\ec601\OpenCV_homework\exercise3\Gaussian2.png',image_smoothing5)

image_smoothing6=image_noise2.copy()
cv2.medianBlur(image_smoothing6,3)
cv2.imshow('Median2',image_smoothing6)
cv2.imwrite('C:\Users\simin\Desktop\ec601\OpenCV_homework\exercise3\Median2.png',image_smoothing6)


cv2.waitKey(0)
cv2.destroyAllWindows()
        
# def main()
#     image = cv2.imread("C:\Users\simin\Desktop\ec601\OpenCV_homework\Test_images\lenna.png")
#     cv2.namedWindow("Original image",CV_WINDOW_AUTOSIZE)
#     cv2.imshow("Original image",image)
    

# skimage.util.random_noise(image, mode='gaussian’, seed=None, clip=True, **kwargs)
# skimage.util.random_noise(image, mode='s&p', seed=None, clip=True, mean = 0)


    


