# Program Cerita Pendek: Dialog Interaktif dengan Operasi Aritmatika
print("SELAMAT DATANG DI PROGRAM SAYA")
# Karakter pertama: halen
nama_helen = "helen"
umur_helen = 22

# Karakter kedua: rangga
nama_rangga = "rangga"
umur_rangga = 20

# Dialog dimulai
print(f"{nama_helen}: Hai {nama_rangga}, bagaimana kabarmu hari ini?")
jawaban_rangga = input(f"{nama_rangga}: ")

print(f"{nama_helen}: Senang mendengarnya! Ngomong-ngomong, umurmu sekarang berapa, {nama_rangga}?")
umur_rangga_input = int(input(f"{nama_rangga}: Aku sekarang berumur {umur_rangga}, kamu berapa, helen? "))

# Menghitung perbedaan umur
selisih_umur = abs(umur_helen - umur_rangga)

print(f"{nama_helen}: Aku berumur {umur_helen} tahun, jadi kita selisih umur {selisih_umur} tahun!")

# Menggunakan operasi aritmatika untuk menghitung total umur
total_umur = umur_helen + umur_rangga
print(f"{nama_helen}: Kalau kita gabungkan umur kita, totalnya jadi {total_umur} tahun!")

# helen ingin membeli buku
print(f"{nama_helen}: Aku ingin membeli 3 buku, harganya masing-masing Rp40.000. Berapa total yang harus kubayar?")
harga_buku = 40000
jumlah_buku = 3
total_harga = harga_buku * jumlah_buku

print(f"{nama_rangga}: Totalnya adalah Rp{total_harga}. Apakah uangmu cukup, helen?")
uang_helen = int(input(f"{nama_helen}: Aku punya uang Rp "))

# Memeriksa apakah uang helen cukup
if uang_helen >= total_harga:
    print(f"{nama_rangga}: Uangmu cukup, kamu bisa membeli bukunya!")
    sisa_uang = uang_helen - total_harga
    print(f"{nama_helen}: Setelah membeli buku, uangku tersisa Rp{sisa_uang}.")
else:
    kekurangan = total_harga - uang_helen
    print(f"{nama_rangga}: Uangmu kurang Rp{kekurangan}. Kamu perlu menabung lebih banyak!")

# Cerita berakhir
print(f"{nama_helen}: Terima kasih atas bantuannya, rangga Sampai jumpa di lain waktu.")
print(f"{nama_rangga}: Sama-sama, helen! Sampai jumpa.")

print("TERIMAKASIH DAN JUMPA LAGI")