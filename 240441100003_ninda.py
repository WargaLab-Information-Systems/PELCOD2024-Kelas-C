# Karakter pertama: ninda
nama_1 = "ninda"
asal_1 ="riau"
# karakter kedua: mawar
nama_2 = "mawar"
asal_2 = "bandung"

print(f"{nama_1} : hallo, {nama_2} apa kabar ?")
jawaba_nnama_2 = input(f"{nama_2} : ")

print(f"{nama_1} : oo iya,aku lupa kamu asal mana ya, {nama_2} ?")
asal_2 = (input(f"{nama_2} : aku dari {asal_2} kamu {nama_1} ?"))
print(f"{nama_1} : aku dari riau ")

# mawar ingin liburan ke rumah ninda yang ada di riau
print(f"{nama_2} : wah kebetulan sekali,besok aku akan liburan ke riau gimana kalau kamu ikut aku?")
print(f"{nama_1} : tapi tiket pesawat sangat mahal")
uang_mawar = int(input(f"{nama_2} : aku punya uang Rp  "))
harga_tiket = 2000000
jumlah_tiket = 2
total_harga = harga_tiket * jumlah_tiket

# Memeriksa jumlah uang untuk membeli tiket pesawat
if uang_mawar >= total_harga:
    print(f"{nama_1} : uangmu cukup, kita bisa pergi!")
    sisa_uang = uang_mawar - total_harga
    print(f"{nama_2} : setalah aku membeli tiket,sisa uangku menjadi Rp{sisa_uang}.")
else:
    kekurangan = total_harga - uang_mawar
    print(f"{nama_1} : Uangmu kurang Rp{kekurangan}!")

# Dialog Penutup
print(f"{nama_1} : gapapa ketika kita pulang nanti aku yang akan membeli tiket")
print(f"{nama_2} : seriusan ini gapapa?")
print(f"{nama_1} : iyaa mawar")
print(f"{nama_2} : baiklah besok aku akan menjemput mu untuk pergi ke bandara")
print(f"{nama_1} : okee,samapi jumpa besok")
