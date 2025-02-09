import cv2 
import matplotlib.pyplot as plt
import numpy as np


# load an image using OpenCV

image = cv2.imread('./images/hero.png')

plt.imshow(image)
plt.axis("off")
plt.show()

# the image is bgr because i didnt conver back to rgb 