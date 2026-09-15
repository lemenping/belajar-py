# ===================================================
# KALKULATOR BERBASIS FUNGSI
# SMK TJP Tuban - Kelas X RPL
# ===================================================

# --- Definisi fungsi operasi ---
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol!"
    return a / b

def pangkat(a, b):
    return a ** b

def modulo(a, b):
    return a % b

# --- Fungsi tampilan ---
def tampilkan_menu():
    print("\n" + "=" * 35)
    print("    KALKULATOR PYTHON")
    print("=" * 35)
    print(" 1. Penjumlahan    (+)")
    print(" 2. Pengurangan    (-)")
    print(" 3. Perkalian      (*)")
    print(" 4. Pembagian      (/)")
    print(" 5. Perpangkatan   (**)")
    print(" 6. Modulo         (%)")
    print(" 0. Keluar")
    print("=" * 35)

# --- Program utama ---
while True:
    tampilkan_menu()
    pilihan = input("Pilih operasi (0-6): ")
    
    if pilihan == '0':
        print("Terima kasih! Program selesai.")
        break
    elif pilihan in ['1', '2', '3', '4', '5', '6']:
        a = float(input("Masukkan angka pertama : "))
        b = float(input("Masukkan angka kedua   : "))

        if pilihan == '1':   hasil = tambah(a, b)
        elif pilihan == '2': hasil = kurang(a, b)
        elif pilihan == '3': hasil = kali(a, b)
        elif pilihan == '4': hasil = bagi(a, b)
        elif pilihan == '5': hasil = pangkat(a, b)
        else:                hasil = modulo(a, b)

        print(f"\nHasil = {hasil}")
    else:
        print("Pilihan tidak valid!")