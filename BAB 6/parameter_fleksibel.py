# Parameter dengan nilai default
def cetak_garis(karakter='=', panjang=30):
    print(karakter * panjang)

cetak_garis()             # pakai default
cetak_garis('-')          # panjang default, karakter '-'
cetak_garis('*', 20)      # kedua argumen diberikan
cetak_garis(panjang=50)   # hanya panjang diganti

# Fungsi *args - menerima banyak argumen
def hitung_total(*harga):
    print(f"Jumlah item: {len(harga)}")
    print(f"Total       : Rp {sum(harga):,}")
    return sum(harga)

hitung_total(15000, 8000, 25000)
hitung_total(50000, 35000, 12000, 8500, 20000)