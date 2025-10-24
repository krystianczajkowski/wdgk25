from PIL import Image
import numpy as np


def rysuj_po_skosie_szare(h, w, a=8, b=10):
    t = (h, w)
    arr = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            arr[i, j] = (a*i + b*j) % 256
    return arr


def main():
    img = Image.open("ob6.png")
    w, h = img.size
    arr = rysuj_po_skosie_szare(h, w)
    imgarr = np.asarray(img).astype(np.uint8)
    arrc = np.ones((h, w, 4), dtype=np.uint8)
    arrc[:, :, 0] = imgarr[:, :, 0]
    arrc[:, :, 1] = imgarr[:, :, 1]
    arrc[:, :, 2] = imgarr[:, :, 2]
    arrc[:, :, 3] = arr[:, :]
    img = Image.fromarray(arrc)
    img.save("ob7.png")
    img.close()


if __name__ == "__main__":
    main()
