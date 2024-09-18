nama1 = "Revan"
nama2 = "Bimo"
alamat1 = "Kediri"
alamat2 = "Malang"
hobi1 = "coding"
hobi2 = "belajar bahasa pemrograman python"
umur1 = 20
umur2 = 18
input("next")
print("Di suatu pagi yang biasa-biasa saja bertemulah dua insan maba yang tidak sengaja bertemu di taman kampus")

print("Revan: Halo, nama saya", nama1)
print("Bimo: Hi, nama saya adalah", nama2)

print("Revan: Wow! nama yang keren, kamu berasal darimana?")
print("Bimo: Aku berasal dari", alamat2)
print("Revan: Hebat, kalau aku dari", alamat1)

print("Bimo: Kamu umur berapa?")
print("Revan: Aku umur", umur1)
print("Bimo: Wah, umur kita hanya beda 2 tahun")
print("Revan: Memang iya? umurmu berapa?")
print("Bimo: Umurku", umur2)
print("Revan: Kita selisih berapa tahun ya?")
input("next")
umur1 = int(input("masukkan umur1 :"))
umur2 = int(input("masukkan umur2 :"))

hasil = umur1 - umur2 

print("hasil dari pengurangan dari", umur1, "dikurangi", umur2, "adalah", hasil)
print("Revan: Ternyata umur kita tidak jauh berbeda")
print("Bimo: Betul!")
print("Revan: Ngomong-ngomong, kamu punya hobi apa?")
print("Bimo: Hobiku", hobi1)
print("Revan: Kalau aku hobinya", hobi2)

Revan = input("Apakah hobi kita sama?")
input("next")
if Revan == "iya":
     print("yaah kamu salah hobi kita beda karena si bimo hobinya" , hobi1 , "dan si revan" , hobi2)
else :
     print("yaps!!!! betul sekali hobi kita beda")

print("Revan: Kalau gitu kita belajar di Perpustakaan Gedung Cakra aja ya")
print("Bimo: Gaaaaaaas!")

print("Akhirnya dua insan maba ini belajar bahasa pemrograman bersama")
