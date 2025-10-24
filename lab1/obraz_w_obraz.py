from PIL import Image
import numpy as np


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
    img_b = Image.open("pasy.bmp")
    img_w = Image.open("inicjaly.bmp")
    img1 = wstaw_obraz_w_obraz(300, 200, 0, 50, img_w, img_b)
    img1.save("wynik.bmp")
    img2 = wstaw_obraz_w_obraz(300, 200, 250, 100, img_w, img_b)
    img2.save("wynik1.bmp")

    img1.close()
    img2.close()
    img_w.close()
    img_b.close()


if __name__ == "__main__":
    main()
