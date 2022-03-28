import airsim 
import numpy as np
import os
import cv2
import time

#https://blog.actorsfit.com/a?ID=00850-7ce2aad1-b508-43ed-8c05-04c7540105b8
#.mat & .npy tutorial

data_array = np.load('normal.npy')
x= np.max(data_array)
y= np.min(data_array)


end=time.time()

print("### 10 million points of data ###")
print("\nData summary:\n", data_array)
print("\nData Shape:\n", data_array.shape)
print(x)
print(y)
