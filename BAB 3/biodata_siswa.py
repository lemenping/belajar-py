# program biodata siswa 
print("=" * 35)
print(" from data siswa ")
print("=" * 35)

nama =input("nama lengkap :")
kelas =input("kelas       :")
umur =int(input("umur (tahun) :"))
tinggi =float(input("tinggi (cm) :"))

print ()
print("=" * 35)
print ( "data tersimpan")
print("=" * 35)
print("nama :",nama)
print("kelas :",kelas)
print("umur :",umur, "tahun")
print("tinggi :", tinggi, "cm")
print("sudah dewasa", umur >= 17)
