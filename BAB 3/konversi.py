# kalkulator koverensi satuan 
print("=== kalkulator koverensi ===")
cm = float(input("masukan panjang (cm):50 "))

# koverernsi ke berbagai sastuan
meter = cm / 100
km = cm /100000
inci = cm / 2.54
kaki = inci / 12

print()
print("cm =", meter, "meter")
print("cm =", km, "kilometer")
print("cm =", round(inci, 2), "inci")
print("cm =", round(kaki, 2), "kaki")