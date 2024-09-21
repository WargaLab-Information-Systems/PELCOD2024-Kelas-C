nama1 = "Marselino" 
nama2 = "Samsul"

hasil = f"{nama1}: halo {nama2}, kamu sudah bayar iuran kas belum?"
print(hasil)
hasil = f"{nama2}: belum nih, {nama1}. aku baru aja kepikiran mau bayar sekarang dikampus"
print(hasil)
hasil = f"{nama1}:bagaimana kalau  kita bayar bareng-bareng aja?"
print(hasil)
hasil = f"{nama2}:boleh, ayok aja mah"
print(hasil)

harga_per_orang = int(input("Samsul: oke, kalau begitu berapa biaya kas nya untuk kita berdua?"))

jumlah_orang = 2
total_biaya = harga_per_orang * jumlah_orang

print(f"Marselino: Kalau kita berdua totalnya jadi {total_biaya} rupiah")

uang_marselino = int(input("Marselino: Aku punya uang "))
uang_samsul = int(input("Samsul: Aku punya uang "))

total_uang = uang_marselino + uang_samsul

print(f"Jadi, total uang kita {total_uang} rupiah")

if total_uang >= total_biaya:
    print("Samsul: Wah, uang kita cukup nih. ayo kita bayar!")
else:
    kekurangan = total_biaya - total_uang
    print(f"Marselino: Sayang sekali, kita masih kurang {kekurangan} rupiah.")
    print("Samsul: mungkin kita perlu menabung dulu, atau bayar pas uang kita cukup saja.")
    print("Marselino: Ya, setuju sih. Mending kita bayar lain kali saja.")