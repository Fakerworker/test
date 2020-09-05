import cv2
from examples import content
import numpy 
import os
import PIL

img = cv2.imread('test.jpg',0)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()