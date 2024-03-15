#EG/2019/3664
#Task1
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def quantize_image(image, levels):
    # Calculate the factor by which to scale intensity levels
    factor = 256 // levels

    # Quantize the image
    quantized_image = (image // factor) * factor

    return quantized_image


# Load the image
image = mpimg.imread('image.jpeg')

# Display the original image
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

# Convert the image to grayscale
gray_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

# Perform quantization
num_levels = int(input("Enter the number of intensity levels (power of 2): "))
quantized_image = quantize_image(gray_image, num_levels)

# Display the quantized image
plt.subplot(1, 2, 2)
plt.imshow(quantized_image, cmap='gray')
plt.title('Quantized Image')
plt.axis('off')

plt.show()
