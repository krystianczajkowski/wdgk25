from PIL import Image
import numpy as np


def rgb_to_cmyk(rgb_array):
    # Przekształć wartości RGB na zakres [0, 1]
    rgb = rgb_array.astype(float) / 255
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    # Oblicz kanał Kk (black)
    k = 1 - np.max(rgb, axis=2)
    # Uniknij dzielenia przez zero
    c = (1 - r - k) / (1 - k + 1e-8)
    m = (1 - g - k) / (1 - k + 1e-8)
    y = (1 - b - k) / (1 - k + 1e-8)
    # Zastąp NaN (dla czystej czerni) zerami
    c[np.isnan(c)] = 0
    m[np.isnan(m)] = 0
    y[np.isnan(y)] = 0
    # Przekształć na zakres [0, 255]
    cmyk = np.stack((c, m, y, k), axis=2) * 255
    return Image.fromarray(cmyk.astype(np.uint8), mode="CMYK")


def main():
    img_rgb = Image.open("ob6.png")
    img_cmyk = Image.open("ob8.tiff")

    arr_rgb = np.asarray(img_rgb).astype(np.uint8)
    arr_cmyk = np.asarray(img_cmyk).astype(np.uint8)
    ch_r = arr_rgb[:, :, 0]
    ch_c = arr_cmyk[:, :, 0]

    print("Typ danych kanału r obrazu RGB: ", ch_r.dtype)
    print("Typ danych kanału c obrazu CMYK: ", ch_c.dtype)
    print("Rozmiar elementu tablicy kanału r obrazu RGB: ", ch_r.itemsize)
    print("Rozmiar elementu tablicy kanału c obrazu CMYK: ", ch_c.itemsize)
    im_r = Image.fromarray(ch_r)
    im_c = Image.fromarray(ch_c)
    print("Tryb kanału r obrazu RGB: ", im_r.mode)
    print("Tryb kanału c obrazu CMYK: ", im_c.mode)
    im_r.save("chR_rgb.png")
    im_c.save("chC_cmyk.png")
    im_r.close()
    im_c.close()
    img_rgb.close()
    img_cmyk.close()


if __name__ == "__main__":
    main()
