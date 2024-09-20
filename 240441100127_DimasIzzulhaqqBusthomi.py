penjual = "Irsyad"
pembeli = "Rifqi"

uang = 20000

# Prolog
print("Di sebuah warung kecil, seorang pembeli datang untuk membeli air mineral dan roti.")
print("Pembeli tersebut membawa uang pas-pasan dan berharap mendapatkan kembalian dari belanjaannya.")
print("Penjual dengan ramah melayani pembeli tersebut, dan terjadilah percakapan sederhana dalam transaksi jual beli.\n")


print(f"{penjual}: Selamat siang, ada yang bisa saya bantu?")
print(f"{pembeli}: Selamat siang. Saya mau beli satu botol air mineral dan satu roti, berapa semuanya?")


air = int(input(f"{penjual}: Harga air mineralnya Rp"))
roti = int(input(f"{penjual}: Harga rotinya Rp"))

hasil = air + roti
kembalian = uang - hasil


print(f"{penjual}: Air mineralnya Rp{air} dan rotinya Rp{roti}. Jadi totalnya Rp{hasil}.")
print(f"{pembeli}: Baik, ini uangnya Rp{uang}.")


if kembalian >= 0:
    print(f"{penjual}: Terima kasih. Ini kembalian Anda Rp{kembalian}. Ada lagi yang ingin dibeli?")
else:
   
    print(f"{penjual}: Maaf, uang Anda kurang Rp{abs(kembalian)}.")


print(f"{pembeli}: Terima kasih, tidak ada. Itu saja.")
print(f"{penjual}: Baik, terima kasih sudah berbelanja. Semoga harimu menyenangkan!")
print(f"{pembeli}: Sama-sama, terima kasih. Sampai jumpa!")
