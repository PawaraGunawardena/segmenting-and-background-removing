from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

def write_frame_output(img_name, img):
    plt.imsave(img_name, img, cmap='gray')

def horizontal_edge_detection(gray):
    sobel_horizontal = np.array([np.array([1, 2, 1]), np.array([0, 0, 0]), np.array([-1, -2, -1])])
    print(sobel_horizontal, 'is a kernel for detecting horizontal edges')
    out_h = ndimage.convolve(gray, sobel_horizontal, mode='reflect')
    write_frame_output("segment_out_h.jpg", out_h)
    plt.imshow(out_h, cmap='gray')

def vertical_edge_detection(gray):
    sobel_vertical = np.array([np.array([-1, 0, 1]), np.array([-2, 0, 2]), np.array([-1, 0, 1])])
    print(sobel_vertical, 'is a kernel for detecting vertical edges')
    out_v = ndimage.convolve(gray, sobel_vertical, mode='reflect')
    write_frame_output("segment_out_v.jpg", out_v)
    plt.imshow(out_v, cmap='gray')

def laplace_edge_detection(gray):
    kernel_laplace = np.array([np.array([1, 1, 1]), np.array([1, -8, 1]), np.array([1, 1, 1])])
    print(kernel_laplace, 'is a laplacian kernel')
    out_l = ndimage.convolve(gray, kernel_laplace, mode='reflect')
    print(out_l)
    write_frame_output("segment_out_l.jpg", out_l)
    plt.imshow(out_l, cmap='gray')

if __name__ == "__main__":
    image = plt.imread('index.png')
    gray = rgb2gray(image)
    horizontal_edge_detection(gray.copy())
    vertical_edge_detection(gray.copy())
    laplace_edge_detection(gray.copy())