# Program Cek Kondisi Nilai
nama  = input("Nama siswa   : ")
nilai = int(input("Nilai ujian : "))
hadir = input("Hadir 80%? (ya/tidak): ")

# Operator perbandingan
print()
print("=== HASIL CEK ===")
print("Nilai >= 75  :", nilai >= 75)
print("Nilai >= 90  :", nilai >= 90)
print("Nilai antara 75-89:", nilai >= 75 and nilai <= 89)

# Operator logika
hadir_ok = hadir == "ya"
lulus    = nilai >= 75 and hadir_ok
remedial = nilai < 75 or not hadir_ok

print("Lulus          :", lulus)
print("Perlu remedial :", remedial)