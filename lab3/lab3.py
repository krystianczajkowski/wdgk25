from PIL import Image
import numpy as np


def rysuj_ramki_szare(w, h, grb):
    ow, oh, color = 0, 0, 0
    arr = np.ones((h, w), dtype=np.uint8)
    while (h - 2*oh) >= grb:
        for i in range(h-2*oh):
            for j in range(grb):
                arr[i+ow][j+ow] = color
            for j in range(w-grb-ow, w-ow):
                arr[i+ow][j] = color
        for i in range(grb):
            for j in range(ow+grb, w-grb-ow):
                arr[i+oh][j] = color
                arr[i+h-grb-oh][j] = color
        ow += grb
        oh += grb
        color = (color + 50) % 255
    return Image.fromarray(arr)


def rysuj_ramke_w_obrazie_ale_na_szaro(obraz, grb):
    color = 127
    arr_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = arr_obraz.shape
    for i in range(h):
        for j in range(grb):
            arr_obraz[i][j] = color
        for j in range(w-grb, w):
            arr_obraz[i][j] = color
    for i in range(grb):
        for j in range(grb, w-grb):
            arr_obraz[i][j] = color
            arr_obraz[i+h-grb][j] = color
    return Image.fromarray(arr_obraz)


def rysuj_pasy_pionowe_szare(w, h, grb):
    color = 127
    t = (h, w)
    arr = np.ones(t, dtype=np.uint8)
    ile = int(w/grb)
    for k in range(ile):
        for g in range(grb):
            i = k * grb + g
            for j in range(h):
                if k % 2:
                    arr[j, i] = color
                else:
                    arr[j, i] = (i/2+j/2) % 256
        color = (color + ile) % 256
    return Image.fromarray(arr)


def rysuj_ramki_kolorowe(w, kolor, zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    t = (w, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    kolor_r = kolor[0]
    kolor_g = kolor[1]
    kolor_b = kolor[2]
    z = w
    for k in range(int(w / 2)):
        for i in range(k, z - k):
            for j in range(k, z - k):
                tab[i, j] = [kolor_r, kolor_g, kolor_b]
        kolor_r = (kolor_r - zmiana_koloru_r) % 256
        kolor_g = (kolor_g - zmiana_koloru_g) % 256
        kolor_b = (kolor_b - zmiana_koloru_b) % 256
    return Image.fromarray(tab)


def negatyw(obraz):
    if (obraz.mode not in ["L", "1", "RGB"]):
        return -1
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    if (obraz.mode != "RGB"):
        tab_obraz ^= 1
        return Image.fromarray(tab_obraz*255)
    w, h, d = tab_obraz.shape
    for i in range(w):
        for j in range(h):
            red = tab_obraz[i][j][0]
            green = tab_obraz[i][j][1]
            blue = tab_obraz[i][j][2]
            tab_obraz[i][j] = [255 - red, 255 - green, 255 - blue]
    return Image.fromarray(tab_obraz)


# formuła zmiany wartości elemntów tablicy a*i + b*j
def rysuj_po_skosie_szare(h, w, a, b):
    t = (h, w)  # rysuje kwadratowy obraz
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a*i + b*j) % 256
    return Image.fromarray(tab)


def koloruj_w_paski(obraz, grub):
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    color_r = 127
    color_g = 0
    color_b = 100
    ile = h//grub
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                if not t_obraz[i, j]:
                    tab[i, j] = [color_r, color_g, color_b]
                else:
                    tab[i, j] = [255, 255, 255]
        color_r = (color_b + color_g) % 256
        color_g = (color_r + color_b) % 256
        color_b = (color_g + color_r) % 256

    return Image.fromarray(tab)


def main():

    img = Image.open("../kc.bmp")
    img = koloruj_w_paski(img, 3)
    img.save("kc.jpg")
    img.close()

    # img = Image.open("gwiazdka.bmp")
    # img = negatyw(img)
    # img.save("gwiazdka_negatyw.bmp")
    # img.close()

    # img = rysuj_ramki_kolorowe(200, [20, 120, 220], 8, 10, -8)
    # img.save("ramki_kolorowe.png")
    # img = negatyw(img)
    # img.save("ramki_kolorowe_negatyw.png")
    # img.close()

    # img = rysuj_po_skosie_szare(100, 300, 8, 10)
    # img.save("szary_skos.png")
    # img = negatyw(img)
    # img.save("szary_skos_negatyw.png")


if __name__ == "__main__":
    main()
