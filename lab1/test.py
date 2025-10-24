import numpy as np
from PIL import Image

im = Image.open("pasy24bit.bmp")

print("Informacje o obrazie")
print("tryb:", im.mode)
print("format:", im.format)
print("rozmiar:", im.size)
print("----------------------------------")
im_data = np.asarray(im)
print("typ danych tablicy", im_data.dtype)
print("rozmiar tablicy", im_data.shape)
print("liczba elementow", im_data.size)
print("wymiar tablicy", im_data.ndim)
print("rozmiar wyrazu tablicy", im_data.itemsize)
print("----------------------------------")
print("pierwszy wyraz", im_data[97][20])
print("----------------------------------")
# print(im_data)

# with open("inicjaly.txt", "w") as f:
#     for row in im_data:
# for i in row:
#     f.write(str(i) + " ")
# f.write("\n")


# im_fd = Image.fromarray(im_data.astype(np.bool))
# print("Informacje o obrazie z tablicy")
# print("tryb:", im_fd.mode)
# print("format:", im_fd.format)
# print("rozmiar:", im_fd.size)
#

def check_pixel(img_data, x, y):
    return img_data[x][y]


# 0 im_fd.show()
# im.show()
