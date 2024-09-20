nama1 = "Naya" 
nama2 = "Martha"

hasil = f"{nama1}: halo {nama2}, kamu sudah makan malam belum?"
print(hasil)
hasil = f"{nama2}: belum nih, {nama1}. aku baru aja kepikiran mau makan di Mawar"
print(hasil)

harga_per_orang = int(input("Naya: Oke, kalau begitu, berapa biaya makannya per orang?"))

jumlah_orang = 2
total_biaya = harga_per_orang * jumlah_orang

print(f"Martha: Kalau ada kita berdua totalnya jadi {total_biaya} rupiah")

uang_naya = int(input("Naya: Aku punya saldo "))
uang_martha = int(input("Martha: Aku punya uang "))

total_uang = uang_naya + uang_martha

print(f"Jadi, total uang kita {total_uang} rupiah")

if total_uang >= total_biaya:
    print("Martha: Wah, uang kita cukup nih. ayo kita makan!")
else:
    kekurangan = total_biaya - total_uang
    print(f"Naya: Sayang sekali, kita masih kurang {kekurangan} rupiah.")
    print("Martha: mungkin kita perlu menabung dulu, atau cari tempat makan yang lebih murah.")
    print("Naya: Ya, setuju. Ayo kita cari tempat makan lain.")