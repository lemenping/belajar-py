berat = int(input("Masukkan Berat Badan Anda (kg): "))
tinggi = float(input("Masukkan Tinggi Badan Anda (cm): "))

BMI = berat / ((tinggi/100)**2)

if (BMI < 18.5):
    kategori = "Kurus (Underweight)"
    keterangan = "Perlu tambah berat badan"
elif (BMI < 24.9):
    kategori = "Normal (Ideal)"
    keterangan = "Pertahankan gaya hidup sehat"
elif (BMI < 29.9):
    kategori = "Gemuk (Overweight)"
    keterangan = "Perlu olahraga lebih"
else:
    kategori = "Obesitas"
    keterangan = "Konsultasi dokter"

print("Nilai BMI  : ", BMI)
print("Kategori   : ", kategori)
print("Keterangan : ", keterangan) 