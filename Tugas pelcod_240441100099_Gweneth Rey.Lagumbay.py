nama1 = "jihan"
nama2 = "gwen"
alamat1 = "tuban"
alamat2 = "malaysia"
tahun = "2024"
tempat = "universitas trunojoyo madura"

print(f"{nama1}: hai salam kenal nama kamu siapa?")
print(f"{nama2}: iya hai namaku {nama2}")

print(f"{nama2}: kalau kamu siapa namanya?")
print(f"{nama1}: nama aku {nama1}")

print(f"{nama1}: asal kamu dari mana {nama2}")
print(f"{nama2}: aku dari {alamat2} kalau kamu?")
print(f"{nama1}: aku dari {alamat1}")

print(f"{nama1}: kamu di {tempat} angkatan berapa?")
print(f"{nama2}: aku angkatan {tahun}")
print(f"{nama1}: ohh sama berarti aku juga dari angkatan {tahun}")

print(f"{nama1}: kamu kan dari {alamat2} kok bisa kuliah di {tempat}?")
print(f"{nama2}: iya karna aku ikut pertukaran pelajar")
print(f"{nama1}: owalah gitu")

print(f"{nama1}: berapa harga tiket dari pp malaysia ke madura?")
print(f"{nama2}: kurang tau sih, ayo kita tanyaian ke loketnya dulu")
print(f"{nama1}: ayo")

hargatiket1 =int(input(f"{nama1}: berapa harga tiket dari malaysia ke madura pak?"))
hargatiket2 =int(input(f"{nama2}: berapa harga tiket dari madura ke malaysia pak?"))

hasil = hargatiket1 + hargatiket2

print("penjualtiket : totalnya", hasil)

harga =str(input(f"{nama1}: ohh ternyata harga tiket pp malaysia madura"))
keamanan =str(input(f"{nama2}: apakah dengan harga segitu keamanannya terjamin?"))
if harga == "murah" and keamanan == "aman":
    print(f"{nama1}: ayo gas beli!")
