import cv2 
import matplotlib.pyplot as plt
import numpy as np


# load an image using OpenCV


# Convert BGR to RGB (OpenCV loads images in BGR by default)
image = cv2.imread('./images/hero.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image)
plt.axis("off")
plt.show()

# the image is bgr because i didnt conver back to rgb 