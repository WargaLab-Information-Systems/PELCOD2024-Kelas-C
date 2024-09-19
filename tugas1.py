print("selamat datang!")
print("mohon masukkan nama karakter")

nama_pengguna1 = input("karakter 1:")
nama_pengguna2 = input("karakter 2:")

print(f"{nama_pengguna1}: hallo {nama_pengguna2} dari mana kamu?")
jalan_jalan = input(f"{nama_pengguna2}:")
print(f"{nama_pengguna1}:oh {jalan_jalan}, kamu sudah makan?")

makan = input(f"{nama_pengguna2}:")
if makan == "sudah":
    print(f"{nama_pengguna1}:oke deh, ayo kita beli makanan ringan saja")
else:
    print(f"{nama_pengguna2}: ayo kita beli kentang goreng!")
input(f"{nama_pengguna1}:")
print(f"{nama_pengguna2}:baiklah, aku sudah langganan diwarung gang depan")
print(f"{nama_pengguna1}:boleh, apakah menunya ada matcha? dan juga aku ingin kentang goreng")
print(f"{nama_pengguna2}:tentu saja ada! ayo kita beli")
print(f"{nama_pengguna1}:jadi berapa harga kentang dan es matcha?")

#operasi aritmatika
angka1 = int(input(f"{nama_pengguna2}:kentang goreng seharga:"))
angka2 = int(input(f"{nama_pengguna2}:es matcha seharga:"))
jumlah = angka1 + angka2
print(f"{nama_pengguna2}:jadi total harga{angka1}dan{angka2}adalah{jumlah}.")
print(f"{nama_pengguna1}:baiklah mari kita membelinya")

    

