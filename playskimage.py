from skimage import io, data, filters
import matplotlib.pyplot as plt
import cv2 as cv


if __name__ == '__main__':
    img = data.coins()
    edges = filters.sobel(img)
    # io.imshow(img)
    # io.show()
    # io.imshow(edges)
    # io.show()
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(img)
    axes[1].imshow(edges)
    fig.show()
