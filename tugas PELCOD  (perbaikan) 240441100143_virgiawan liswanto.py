nama1 = "egy"
nama2 = "ali"
nama3 = "kasir"
alamat1 = "bangkalan"
alamat2 = "sumenep"
angkatan = 24
angkatan = 24
tempat = "toko buku"

print(f"{nama1}: siapa namamu?")
print(f"{nama2}: namaku {nama2}")

print(f"{nama2}: dan siapa namamu? ")
print(f"{nama1}: namaku {nama1}") 

print(f"{nama1}: apa kamu baru di universitas ini?")
print(f"{nama2}: iya aku mahasiswa baru angkatan {angkatan}")

print(f"{nama1}: ingin kemana kamu pagi-pagi begini?")
print(f"{nama2}: aku ingin pergi ke {tempat}")

print(f"{nama1}: boleh aku ikut dengan mu?")
print(f"{nama2}: tentu ayo pergi bersama")

print("Dan akhirnya mereka ke toko buku bersama")
print(f"{nama1}:buku ini keliatan seruu")
print(f"{nama2}:mari lihat dulu")


harga =str(input(f"{nama1}:bagaimana harganya?"))
kualitas =str(input(f"{nama2}:bagaimana kualitas nya?"))
if harga == "murah" and kualitas =="bagus":
    print(f"{nama1}:ayoo belii")
else :
    print("malasss cari yang lain")

print(f"{nama1}: ayo kita tanyakan harganya dulu")
print(f"{nama2}: ayo pergi ke kasir nya dulu")



hargabuku1 =int(input(f"{nama1}:berapa harga buku saya buk. {nama3}:"))
hargabuku2 =int(input(f"{nama2}:berapa harga bukunya mpok. {nama3}:"))

hasil = hargabuku1 + hargabuku2

bukuegy = 25
bukuali = 25

print(f"{nama3} :jadi total nya", hasil)



 
