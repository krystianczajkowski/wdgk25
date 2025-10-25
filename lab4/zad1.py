from PIL import Image
import numpy as np


def rysuj_pionowe_szare(w, h, grb, arr):
    color = 127
    ile = int(w/grb)
    for k in range(ile):
        for g in range(grb):
            j = k * grb + g
            for i in range(h):
                arr[i][j] = color

        color = (color + ile) % 200  # tylko do 200 bo biały razi w oczy
    return arr


def rysuj_rgb_pasami(w, h):
    t = (h, w, 3)
    arr = np.ones(t, dtype=np.uint8)
    arr[:, :, 0] = rysuj_pionowe_szare(w, h, 10, arr[:, :, 0])
    arr[:, :, 1] = rysuj_pionowe_szare(w, h, 18, arr[:, :, 1])
    arr[:, :, 2] = rysuj_pionowe_szare(w, h, 26, arr[:, :, 2])
    return Image.fromarray(arr)


def rysuj_r(w, h):
    t = (h, w, 3)
    arr = np.ones(t, dtype=np.uint8)
    arr[:, :, 0] = rysuj_pionowe_szare(w, h, 10, arr[:, :, 0])
    return Image.fromarray(arr)


def rysuj_g(w, h):
    t = (h, w, 3)
    arr = np.ones(t, dtype=np.uint8)
    arr[:, :, 1] = rysuj_pionowe_szare(w, h, 18, arr[:, :, 1])
    return Image.fromarray(arr)


def rysuj_b(w, h):
    t = (h, w, 3)
    arr = np.ones(t, dtype=np.uint8)
    arr[:, :, 2] = rysuj_pionowe_szare(w, h, 26, arr[:, :, 2])
    return Image.fromarray(arr)


def main():
    img = rysuj_r(300, 200)
    img.show()
    img.save("obR.png")
    img.close()

    img = rysuj_g(300, 200)
    img.show()
    img.save("obG.png")
    img.close()

    img = rysuj_b(300, 200)
    img.show()
    img.save("obB.png")
    img.close()


if __name__ == "__main__":
    main()
