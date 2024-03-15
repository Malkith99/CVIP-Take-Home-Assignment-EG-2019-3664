#EG/2019/3664
#Task2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.signal import convolve2d


def spatial_average(image, neighborhood_size):
    # Define the kernel for averaging
    kernel = np.ones((neighborhood_size, neighborhood_size)) / (neighborhood_size ** 2)
    # Perform 2D convolution to compute the spatial average
    averaged_image = convolve2d(image, kernel, mode='same', boundary='symm')
    return averaged_image


# Load the image
image = mpimg.imread('image.jpeg')

# Display the original image
plt.figure(figsize=(12, 4))
plt.subplot(1, 4, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

# Convert the image to grayscale
gray_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

# Define neighborhood sizes
neighborhood_sizes = [3, 10, 20]

# Perform spatial averaging for each neighborhood size
for i, size in enumerate(neighborhood_sizes):
    # Perform spatial averaging
    averaged_image = spatial_average(gray_image, size)

    # Display the averaged image
    plt.subplot(1, 4, i + 2)
    plt.imshow(averaged_image, cmap='gray')
    plt.title('Averaged Image ({:d}x{:d})'.format(size, size))
    plt.axis('off')

plt.show()
