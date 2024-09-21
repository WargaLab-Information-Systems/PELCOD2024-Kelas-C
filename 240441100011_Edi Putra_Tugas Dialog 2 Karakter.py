# Dialog antara dua karakter: Edi dan putra
# Menggunakan variabel, tipe data, operasi aritmatika, operasi logika, dan input pengguna.

# Pendefinisian variabel awal
nama1 = "Edi"
nama2 = "Putra"

# Dialog pembuka
print(f"{nama1}: 'eeuuyy {nama2}, gimana kabarmu?'")
print(f"{nama2}: 'eh, hai{nama1} aku baik. Kamu gimana?'")

# edi menanyakan apakah putra sudah makan
sudah_makan = input(f"{nama1}: 'baik juga. Oh ya, kamu dah makan belum? (jawab udah/belum)' ").lower()

if sudah_makan == 'udah':
    print(f"{nama2}: 'Iya, aku udah makan.'")
else:
    print(f"{nama2}: 'Belum nih, masih sibuk nugas tadi.'")

# Operasi Aritmatika - Hitung biaya makanan
harga_makanan = 10  # Asumsikan harga makanan adalah 10 ribu rupiah
jumlah_porsi = int(input(f"{nama1}: 'Kalau kamu mau makan nanti ama aku, mau pesan berapa porsi? '"))
total_biaya = harga_makanan * jumlah_porsi
print(f"{nama2}: 'Hmm, kalau pesan {jumlah_porsi} porsi, biayanya bakal jadi {total_biaya} ribu rupiah ya.'")

# edi menawarkan untuk membayar setengah
setuju = input(f"{nama1}: 'Gimana kalau kita patungan? Aku bisa bayar setengah, oke? (jawab ya/tidak): ' ").lower()

if setuju == 'ya':
    biaya_per_orang = total_biaya / 2
    print(f"{nama2}: 'Oke, setuju. Jadi masing-masing bayar {biaya_per_orang} ribu rupiah.'")
else:
    print(f"{nama2}: 'Gak perlu, aku bisa bayar sendiri kok.'")

# Penutup dengan logika tambahan
print(f"{nama1}: 'Woke. Eh, nanti lanjut nonton film yok enaknya jam berapa ya?'")
putra_setuju_nonton = input(f"{nama2}: 'gasss! mending Jam (masukkan angka jam):'")

# Operasi logika untuk mengecek waktu nonton
if int(putra_setuju_nonton) > 20:
    print(f"{nama1}: 'Waduh, kalau jam {putra_setuju_nonton} terlalu malam keknya, besok aj lah!'")
else:
    print(f"{nama1}: 'Oke, jam {putra_setuju_nonton} pas, jan lupa ya! '")