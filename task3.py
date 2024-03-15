#EG/2019/3664
#Task3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import ndimage

# Load the image
image = mpimg.imread('image.jpeg')

# Display the original image
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

# Rotate the image by 45 degrees
rotated_image_45 = ndimage.rotate(image, 45, reshape=True)
plt.subplot(1, 3, 2)
plt.imshow(rotated_image_45)
plt.title('Rotated by 45 Degrees')
plt.axis('off')

# Rotate the image by 90 degrees
rotated_image_90 = ndimage.rotate(image, 90, reshape=True)
plt.subplot(1, 3, 3)
plt.imshow(rotated_image_90)
plt.title('Rotated by 90 Degrees')
plt.axis('off')

plt.show()
