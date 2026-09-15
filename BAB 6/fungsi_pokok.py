# fungsi tanpa parameter dan tanpa return
def garis_pemisah():
    print("=" * 35)

# fungsi dengan parameter dan tanpa return
def sapa_siswa(nama, kelas):
    print(f"Halo, {nama} dari kelas {kelas}!.")

    # fungsi dengan parameter dan return
def hitung_luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

def hitung_keliling_persegi(sisi):
    return 4 * sisi

#    memanggil semua fungsi
garis_pemisah()
sapa_siswa("Budi", "X RPL")
sapa_siswa("Ani", "X RPL")
garis_pemisah()

l_segitiga = hitung_luas_segitiga(10, 6)
print(f"Luas segitiga: (alas=10, tinggi=6) : {l_segitiga}")

k_persegi = hitung_keliling_persegi(7)
print(f"keliling persegi (sisi=7) : {k_persegi}")

#   Fungsi langsung dalam persegi
print(f"total luas + keliling {l_segitiga + k_persegi}")