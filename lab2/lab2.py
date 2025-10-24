from PIL import Image
import numpy as np
from math import sin, cos, pi


def rysuj_ramke_w_obrazie(obraz, grb):
    arr_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = arr_obraz.shape
    for i in range(h):
        for j in range(grb):
            arr_obraz[i][j] = 0
        for j in range(w-grb, w):
            arr_obraz[i][j] = 0
    for i in range(grb):
        for j in range(grb, w-grb):
            arr_obraz[i][j] = 0
            arr_obraz[i+h-grb][j] = 0
    arr = arr_obraz.astype(bool)
    return Image.fromarray(arr)


def rysuj_ramke_w_obrazie_inaczej(obraz, ow, oh, grb, color):
    arr_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = arr_obraz.shape
    while (h - 2*oh) >= grb:
        for i in range(h-2*oh):
            for j in range(grb):
                arr_obraz[i+ow][j+ow] = color
            for j in range(w-grb-ow, w-ow):
                arr_obraz[i+ow][j] = color
        for i in range(grb):
            for j in range(ow+grb, w-grb-ow):
                arr_obraz[i+oh][j] = color
                arr_obraz[i+h-grb-oh][j] = color
        ow += grb
        oh += grb
        color = color ^ 1
    return Image.fromarray(arr_obraz * 255)


def rysuj_ramki(h, w, grb):
    arr = np.ones((h, w), dtype=np.uint8)
    img = Image.fromarray(arr)
    img = rysuj_ramke_w_obrazie_inaczej(
        img, 0, 0, grb, color=0)
    return img


def rysuj_pasy_poziome(w, h, grub):  # w, h   -  rozmiar obrazu
    t = (h, w)  # rozmiar tablicy
    tab = np.ones(t, dtype=np.uint8)
    # jaki bedzie efekt, gdy np.ones zamienimy na np.zeros?
    ile = int(h/grub)  # liczba pasów  o grubości grub
    for k in range(ile):  # uwaga k = 0,1,2..   bez ile
        for g in range(grub):
            i = k * grub + g  # i - indeks wiersza, j - indeks kolumny
            for j in range(w):
                tab[i, j] = k % 2  # reszta z dzielenia przez dwa
    tab = tab * 255
    return Image.fromarray(tab)


def rysuj_pasy_pionowe(w, h, grb):
    t = (h, w)
    arr = np.ones(t, dtype=np.uint8)
    ile = int(w/grb)
    for k in range(ile):
        for g in range(grb):
            i = k * grb + g
            for j in range(h):
                arr[j, i] = k % 2
    arr = arr * 255
    return Image.fromarray(arr)


def rysuj_wlasne(w, h, grb):
    arr = np.ones((w, h), dtype=np.uint8)
    mx = w//2
    my = h//2
    for i in range(361):
        x = mx + int(5*grb*sin(pi*i/180))
        y = my + int(5*grb*cos(pi*i/180))
        arr[x, y] = 0
        for j in range(4*grb):
            arr[x-2*j, y-j] = 0
    arr = arr * 255
    return Image.fromarray(arr)


def rysuj_paski(obraz, grb):
    arr_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = arr_obraz.shape
    for i in range(h):
        for j in range(grb):
            arr_obraz[i][j] = 0
        for j in range(w-grb, w):
            arr_obraz[i][j] = 0
    arr = arr_obraz.astype(bool)
    return Image.fromarray(arr)


def wstaw_obraz_w_obraz(w, h, m, n, obraz, ob2):
    tab_obraz = np.asarray(obraz).astype(np.int_)
    h0, w0 = tab_obraz.shape
    tab = np.asarray(ob2).astype(np.int_)
    # jesli wstawiany obraz wychodzi poza ramy nowego obrazu, to przycinamy
    n_k = min(h, n + h0)
    # jesli wstawiany obraz wychodzi poza ramy nowego obrazu, to przycinamy
    m_k = min(w, m + w0)
    # jesli miejsce wstawienia jest ujemne(wychodzi poza nowy obraz w górę), to przycinamy
    n_p = max(0, n)
    # jesli miejsce wstawienia jest ujemne(wychodzi poza nowy obraz w lewo), to przycinamy
    m_p = max(0, m)
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab[i][j] = tab_obraz[i - n][j - m]
    # zapisanie tablicy w typie bool (obrazy czarnobiałe)
    tab = tab.astype(bool)
    return Image.fromarray(tab)


def main():
    # wlasne
    # img = rysuj_wlasne(300, 300, 8)
    # img.save("wlasne.bmp")
    # img.close()

    # ramki
    # img = rysuj_ramki(80, 130, 5)
    # img.save("ramka.bmp")
    # img.close()

    # ramka tablica.bmp
    # img = Image.open("tablica.bmp")
    # img = rysuj_ramke_w_obrazie(img, 50)
    # img.save("tablica_ramka.bmp")
    # img.close()
    img = rysuj_pasy_pionowe(200, 100, 10)
    # img.save("pasy.bmp")
    img.show()
    img.close()


if __name__ == "__main__":
    main()
