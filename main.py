import cv2
import numpy as np
import function

img=cv2.imread('lenna.png',cv2.IMREAD_GRAYSCALE)
img2=cv2.imread('lenna.png',cv2.IMREAD_GRAYSCALE)
img3=cv2.imread('lenna.png',cv2.IMREAD_GRAYSCALE)
data=[[1,2,1]]
data2=[[1],[2],[1]]
arr=np.array(data)
arr2=np.array(data2)
#arr=arr
#arr2=arr2
data3=[[1,2,1],[2,4,2],[1,2,1]]
arr3=np.array(data3)
#arr3=arr3

img=function.cross_correlation_1d(img,arr2)
img=function.cross_correlation_1d(img,arr)
img2=function.cross_correlation_2d(img2,arr3)
#img2=cv2.normalize(img2,None,alpha=0,beta=255,norm_type=cv2.NORM_MINMAX,dtype=cv2.CV_8U)
a=img.sum()-img2.sum()
print(a)
print(img)
print(img2)
cv2.imshow('after1d',img)
cv2.imshow('after2d',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()