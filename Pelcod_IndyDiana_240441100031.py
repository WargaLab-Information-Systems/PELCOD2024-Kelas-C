print("Dialog dengan 2 karakter, menggunakan operasi aritmatika dan logika beserta input dari pengguna")
print("mohon masukkah nama karakter")

nama_pengguna1 = input("karakter 1:")
nama_pengguna2 = input("karakter 2:")

print(f"{nama_pengguna1}: hai {nama_pengguna2} dari mana?")
kegiatan = input(f"{nama_pengguna2}:")
print(f"{nama_pengguna1}: ohh {kegiatan}, ngomong ngomong tugas matematika sudah?")

tugas = input(f"{nama_pengguna2} :")
if tugas == "sudah":
    print(f"{nama_pengguna1}: nomor berapa yang menurutmu sulit?")
else:
    print(f"{nama_pengguna1}: nomor berapa yang belum? biar aku bantu!")

nomor_tugas = input(f"{nama_pengguna2}: ")
print(f"{nama_pengguna1}: oh! nomor {nomor_tugas} tentang pembagian bukan?")
print(f"{nama_pengguna2}: iya!")
print(f"{nama_pengguna1}: sepertinya aku ingat soal dan jawabannya")
print(f"{nama_pengguna2}: benarkah? bisakah kamu menjelaskannya?")
print(f"{nama_pengguna1}: tentu!")

angka1 = int(input(f"{nama_pengguna1}: angka pertama yaitu "))
angka2 = int(input(f"{nama_pengguna1}: dibagi dengan"))
bagi = angka1 / angka2 if angka2 != 0 else "Tidak bisa dibagi dengan nol"
print(f"{nama_pengguna1}: jadi hasil dari {angka1} dibagi {angka2} sama dengan {bagi}")
print(f"{nama_pengguna2}: ah begitu! baiklah {nama_pengguna1} terima kasih penjelasannya")
print(f"{nama_pengguna1}: aman kok! sampai jumpa {nama_pengguna2}!")
