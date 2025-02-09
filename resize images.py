import matplotlib.pyplot as plt
import cv2 
import numpy as np 


# load the image 

# Convert BGR to RGB (OpenCV loads images in BGR by default)
image = cv2.imread('./images/hero.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
resized_image = cv2.resize(image, (400, 400)) 
plt.imshow(resized_image)
plt.axis("off")
plt.show()