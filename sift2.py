#python
import cv2
from scipy.misc import imread, imsave, imresize
import numpy as np
from time import sleep
image = cv2.imread("/home/seenu/Desktop/panorama.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
q= imresize(gray,(100,100))
sift = cv2.xfeatures2d.SIFT_create()
(kps, descs) = sift.detectAndCompute(q, None)

w,h = descs.shape   # it will give us the shape of the descriptor
n=np.zeros((w,h)) 
x=np.zeros((w,h))
n=np.array(descs)
s=np.array(x)
a=n.shape
print(n.shape)
print(x.shape)
#sleep(2)
for i in range(w):
        for j in range(h):
                x[i,j] = n[i,j]
                
            
np.savetxt("foo.csv", x, delimiter=",")  ## here we are saving the SIFT descriptor in a csv file

print(x)

