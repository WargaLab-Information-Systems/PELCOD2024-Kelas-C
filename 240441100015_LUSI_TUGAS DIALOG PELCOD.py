print("Pada suatu hari terdapat dua orang sahabat yang ingin merencanakan mendaki gunung bersama")
print("Lusi: ")
orang1 = input(":")
print("Meta: ")
orang2 = input(":")
tempat_mendaki = input("Tempat mendaki yang akan dikunjungi:")
tanggal_berangkat = input("Tanggal berangkat: ")
tanggal_pulang = input("Tanggal pulang: ")
jam_berangkat = input("Jam berangkat: ")
jam_pulang = input("Jam pulang: ")
jarak_tempuh = input("Jarak tempuh ke tempat Mendaki (dalam km): ")
waktu_tempuh = input("Waktu tempuh (dalam jam): ")

print("===============================================")
print(orang1, ":Besok kita mau kemana?")
print(orang2, ":Loh... kamu lupa kita mau", tempat_mendaki)
print(orang1, ":Kita berangkat kapan?")
print(orang2, ":Kita berangkat pada tanggal", tanggal_berangkat, "pukul", jam_berangkat)
print(orang1, ":Terus pulangnya kapan?")
print(orang2, ":Kita pulang pada tanggal", tanggal_pulang, "pukul", jam_pulang)
print(orang1, ":Berapa jauh jarak yang kita tempuh?")
print(orang2, ":Jarak yang kita tempuh itu sekitar", jarak_tempuh, "km")
print(orang1, ":Kalo boleh tau berapa lama perjalanannya?")
print(orang2, ":Waktu yang kita tempuh itu sekitar", waktu_tempuh, "jam")

# Menghitung apakah waktu tempuh sesuai dengan jarak tempuh
jarak = float(jarak_tempuh)
waktu = float(waktu_tempuh)
rata_rata_kecepatan = jarak / waktu

hasil = tanggal_berangkat == tanggal_pulang
print("apakah tanggal berangkat sama dengan tanggal pulang")
print(hasil)