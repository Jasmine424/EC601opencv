
# coding: utf-8

# In[ ]:



"""
copyright Simin Zhai siminz@bu.edu
"""
import cv2
import numpy as np

emma = cv2.imread('C:\Users\simin\Desktop\ec601\OpenCV_homework\Test_images/emma.png') 
# pixel1=emma[20,25,0]
# pixel2=emma[20,25,1]
# pixel3=emma[20,25,2]
[b,g,r] = cv2.split(emma)
pixel1=b[20,25]
pixel2=g[20,25]
pixel3=r[20,25]
print("blue pixel value", pixel1)
print("Green pixel value", pixel2)
print("red pixel value", pixel3)


cv2.imshow('Blue',b)
cv2.imwrite('C:\Users\simin\Desktop\ec601\OpenCV_homework\exercise2\Blue.png',b)
cv2.imshow('Red',r) 
cv2.imwrite('C:\Users\simin\Desktop\ec601\OpenCV_homework\exercise2\Red.png',r)
cv2.imshow('Green',g)
cv2.imwrite('C:\Users\simin\Desktop\ec601\OpenCV_homework\exercise2\Green.png',g)


hsv_emma = cv2.cvtColor(emma, cv2.COLOR_BGR2HSV) 

[h,s,v] = cv2.split(hsv_emma) 

pixel4=h[20,25]
pixel5=s[20,25]
pixel6=v[20,25]
print("H pixel value", pixel4)
print("S pixel value", pixel5)
print("V pixel value", pixel6)


cv2.imshow('Hue',h)
cv2.imwrite('C:\Users\simin\Desktop\ec601\OpenCV_homework\exercise2\Hue.png',h)
cv2.imshow('Saturation',s)
cv2.imwrite('C:\Users\simin\Desktop\ec601\OpenCV_homework\exercise2\Saturation.png',s)
cv2.imshow('Value',v)
cv2.imwrite('C:\Users\simin\Desktop\ec601\OpenCV_homework\exercise2\Value.png',v)

YCC_emma = cv2.cvtColor(emma, cv2.COLOR_BGR2YCR_CB) #convert to YCrCb

[y,Cb,Cr] = cv2.split(YCC_emma) #split YCrCb channels

pixel7=y[20,25]
pixel8=Cb[20,25]
pixel9=Cr[20,25]
print("Y pixel value", pixel7)
print("Cb pixel value", pixel8)
print("Cr pixel value", pixel9)

cv2.imshow('Y',y)
cv2.imwrite('C:\Users\simin\Desktop\ec601\OpenCV_homework\exercise2\Y.png',y)
cv2.imshow('Cb',Cb)
cv2.imwrite('C:\Users\simin\Desktop\ec601\OpenCV_homework\exercise2\Cb.png',Cb)
cv2.imshow('Cr',Cr)
cv2.imwrite('C:\Users\simin\Desktop\ec601\OpenCV_homework\exercise2\Cr.png',Cr)

cv2.waitKey(0)
cv2.destroyAllWindows()  

