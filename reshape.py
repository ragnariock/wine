import re
import os
import cv2

num = 1

width = 800
height = 800
dim = (width, height)
 

for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
      nameImage = os.path.join(root,name)
      nameImage = str(nameImage)
      if re.search(r'jpg',nameImage):
      	img = cv2.imread(nameImage)
      	
      	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

      	cv2.imwrite('image/'+str(num) + '.jpg',resized)
      	num +=1

print(num)