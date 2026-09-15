# parameter biasa
def luas_persegi_panjang(panjang, lebar):
    print("luas:", panjang * lebar)

luas_persegi_panjang(8, 5)          # argumen posisional
luas_persegi_panjang(lebar=4, panjang=6)  # keyword argument

# nilai default
def sapa(nama, salam="Halo"):
    print(salam + ", " + nama + "!")

    sapa('Budi')  # output: Halo, Budi!
    sapa('Ani', 'Selamat pagi')  # output: Selamat pagi, Ani!