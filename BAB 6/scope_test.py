# bagian A
pesan = 'saya variabel global'

def tampilkan():
    print(pesan)            # pakai variabel global

    tampilkan()
    print(pesan)

# bagian B
angka = 100

def ubah_lokal():
    angka = 999             # variabel lokal berbeda dari - variabel global!
    print("Didalam_fungsi:", angka)

ubah_lokal()
print("Diluar_fungsi:", angka)


