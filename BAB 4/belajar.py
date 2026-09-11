total = int(input ('total belanja'))

if(total >= 500000):
    diskon = 0,2
else:
    if(total >=200000):
        diskon = 0,1
    else :
        diskon = 0

bayar = total - (total * diskon)   
print("total : ", total)
print("diskon : ", diskon)
print("bayar : ", bayar)

