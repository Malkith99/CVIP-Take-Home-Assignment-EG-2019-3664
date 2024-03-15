#EG/2019/3664
#Task4
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def reduce_resolution(image, block_size):
    # Get dimensions of the image
    height, width = image.shape

    # Calculate number of blocks in each dimension
    num_blocks_height = height // block_size
    num_blocks_width = width // block_size

    # Reshape the image into blocks
    blocks = image[:num_blocks_height * block_size, :num_blocks_width * block_size].reshape(
        num_blocks_height, block_size, num_blocks_width, block_size
    )

    # Compute the average of each block
    averaged_blocks = blocks.mean(axis=(1, 3))

    # Repeat the averaged blocks to reconstruct the reduced image
    reduced_image = np.repeat(np.repeat(averaged_blocks, block_size, axis=1), block_size, axis=0)

    return reduced_image


# Load the image
image = mpimg.imread('image.jpeg')

# Convert the image to grayscale
gray_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

# Define block sizes
block_sizes = [3, 5, 7]

# Perform reduction for each block size
plt.figure(figsize=(12, 4))
for i, size in enumerate(block_sizes):
    reduced_image = reduce_resolution(gray_image, size)
    plt.subplot(1, len(block_sizes), i + 1)
    plt.imshow(reduced_image, cmap='gray')
    plt.title('Block Size: {}x{}'.format(size, size))
    plt.axis('off')

plt.show()
