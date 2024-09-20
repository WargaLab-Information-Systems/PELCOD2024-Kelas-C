# Program dialog antara dua karakter: Alice dan Bob

# Menyapa pengguna
print("Selamat datang di program dialog antara eko dan turam!")
print("eko: Halo ram, Hari ini kita akan belajar berhitung dengan matematika.")
print("turam: Hai eko Aku paling semangat kalo soal matematika!")
print("eko: yaudah lansung aku mulai yaa")
print("turam: okee")

# Mengambil input dari pengguna untuk angka
try:
    angka1 = float(input("eko: Berikan aku angka pertama: "))
    angka2 = float(input("eko: Berikan aku angka kedua: "))
except ValueError:
    print("tolong masukkan angka yang valid.")
    exit()


# Melakukan operasi aritmatika
jumlah = angka1 + angka2
selisih = angka1 - angka2
produk = angka1 * angka2

if angka2 != 0:
    pembagian = angka1 / angka2
else:
    pembagian = None

# Menampilkan hasil operasi aritmatika
print("\neko: Aku sudah melakukan beberapa perhitungan.")
print(f"eko: Jumlah dari {angka1} dan {angka2} adalah {jumlah}.")
print(f"eko: Selisih antara {angka1} dan {angka2} adalah {selisih}.")
print(f"eko: Produk dari {angka1} dan {angka2} adalah {produk}.")

if pembagian is not None:
    print(f"eko: Pembagian dari {angka1} oleh {angka2} adalah {pembagian}.")
else:
    print("eko: Pembagian dengan nol tidak diperbolehkan.")

# Operasi logika
if angka1 > angka2:
    print(f"\neko: {angka1} lebih besar dari {angka2}.")
elif angka1 < angka2:
    print(f"eko: {angka1} lebih kecil dari {angka2}.")
else:
    print(f"eko: {angka1} sama dengan {angka2}.")

# Mengakhiri dialog
print("\nturam: Terima kasih, eko! Ini sangat membantu.")
print("eko: Sama-sama, turam! Sampai jumpa di pelajaran matemattika berikutnya!")
print("turam: okeee")