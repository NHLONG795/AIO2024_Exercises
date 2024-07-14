import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread("./Exs_7_6_w1/dog.jpeg")

# HACK: Lightness way (max(rgb) + min(rgb))/2
gray_img_01 = (np.amax(img, axis=2) + np.amin(img, axis=2)) / 2
# print(gray_img_01[0,0])

# HACK: Average way sum(rgb)/3
gray_img_01 = np.sum(img, axis=2) / 3
# print(gray_img_01[0,0])

# HACK: Luminosity way sum(param * rgb)
paramater_arr = np.array([0.21, 0.72, 0.07])
gray_img_01 = np.sum(np.multiply(paramater_arr, img), axis=2)
print(gray_img_01[0,0])
