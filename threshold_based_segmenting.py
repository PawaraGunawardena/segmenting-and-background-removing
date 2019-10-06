from skimage.color import rgb2gray
import matplotlib.pyplot as plt

def write_frame_output(img_name, img):
    plt.imsave(img_name, img, cmap='gray')

def single_threshold(gray):
    gray_r = gray.reshape(gray.shape[0]*gray.shape[1])
    for i in range(gray_r.shape[0]):
        if gray_r[i] > gray_r.mean():
            gray_r[i] = 1
        else:
            gray_r[i] = 0
    gray = gray_r.reshape(gray.shape[0],gray.shape[1])
    write_frame_output("gray_single_threshold.jpg", gray)

def multi_threshold(gray):
    gray_r = gray.reshape(gray.shape[0]*gray.shape[1])
    for i in range(gray_r.shape[0]):
        if gray_r[i] > gray_r.mean():
            gray_r[i] = 3
        elif gray_r[i] > 0.5:
            gray_r[i] = 2
        elif gray_r[i] > 0.25:
            gray_r[i] = 1
        else:
            gray_r[i] = 0
    gray = gray_r.reshape(gray.shape[0],gray.shape[1])
    write_frame_output("gray_multiple_threshold.jpg", gray)

if __name__ == "__main__":
    image_name = "1.jpeg"
    image = plt.imread(image_name)

    gray = rgb2gray(image)
    single_threshold(gray.copy())
    multi_threshold(gray)