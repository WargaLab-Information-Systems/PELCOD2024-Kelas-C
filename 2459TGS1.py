#input nama
nama_satu =  input("Masukan nama pemilik program!")
nama_dua = input("Masukan nama anda!")


print(f"Hari ini {nama_satu} berencana ke toko yang baru buka disebelah gang rumahnya. saat tiba ditoko {nama_satu} seperti melihat seseorang yang tidak asing baginya, tanpa merasa ragu {nama_satu} mulai menyapanya. ")


# dialog prtma
print(f"{nama_satu}: Hai, {nama_dua}?. ")
print(f"{nama_dua}: Eh halo {nama_satu}, kebetulan banget kita ketemu disini ")
print(f"{nama_satu}: Wah iya mampir nih deket dari rumah jadi mampir, oh iya kamu beli apa disni?.")


# menentukan barang yang akan di beli
nama_barang = input ("Masukan nama barang!")
uangnamasatu = 120
uangnamakedua = 75
print(f"{nama_dua}: Aku rencananya sih kepengen beli {nama_barang} nih.")
print(f"{nama_satu}: Trus kenapa diam disini?.")
print(f"{nama_dua}: lagi mikir, Kayanya uangku kurang deh, aku balik dulu mau ambil uang.")
print(f"{nama_satu}: Dari pada balik mending nih pinjam aja uangku, karna lucu aku juga mau {nama_barang}nya deh, sekalian bayar punyaku ya.")
print(f"{nama_dua}: Yakan?, eh tapi bener boleh pinjam uangmu nih?.")
print(f"{nama_satu}: iya sekalian aja.")
print(F"{nama_dua}: Maaf ya kupinjam dulu uangmu.")
print(f"{nama_satu}: Gapapa kok santai aja, kamu ada uang berapa?.")
print(f"{nama_dua} : aku punya uang {uangnamakedua}ribu nih.")
print(F"{nama_satu}: aku ada {uangnamasatu}ribu.")

# total uang yang sekarang dimiliki
total_uang = uangnamasatu + uangnamakedua
print(f"{nama_dua}: kalo uangnya kita gabungin terkumpul {total_uang}ribu." )


# bandingkan uang 
uangsatu = input(f"Apakah uang {nama_dua} lebih banyak dari uang {nama_satu}?.")
uangdua = input(f"Apakah justru uang {nama_satu} lebih banyak?.")
if uangsatu == "tidak" or "salah" and uangdua == "benar" or "iya" :
    print(f"Ya, benar sekali uang {nama_satu} lebih banyak dari uang {nama_dua} . sekarang mari kita lihat harga barangnya!.")

# masukan harga barang 
harga_barang = 80
jumlah_orang = 2
print(f"{nama_satu}: Untuk harga {nama_barang} senilai {harga_barang}ribu nih.")
print(f"{nama_dua}: Apa cukup dengan harga {harga_barang}ribu, dengan uang yang kita punya?.")

# memasukan harga barang dan jumlah orangnya
total_barang = harga_barang * jumlah_orang
print(f"{nama_satu}: Totalnya untuk dua orang {total_barang}ribu.")
print(f"{nama_dua}: Wah masi ada lebih dong!.")
#print(f"{nama_satu}: Eh tapi adaa diskon nih, untuk pembelian dua.")
#print(f"{nama_dua}: Mayan tuh berapa diskon nya?.")
#print(f"{nama_satu}: 20%")

# total haraga setelah dapat diskon
#diskon = input("Berapa diskonnya?") #20
#harga_sebelumnya =input("berapa harga asli barang tsb?") # 80

#if diskon == 20 and harga_sebelumnya == 80:
 #   print("berapakah harga potongan yang didapatkan?")
#ttldiskon = input("Jawab!")

#cara = diskon  harga_sebelumnya
#print (f"jawaban yang benar adalah {cara}.")

sisa = total_uang - total_barang
print(f"{nama_satu}: Nyisa berapa uangnya?.")
print(f"{nama_dua}: {sisa}ribu nih.")
print(f"{nama_satu}: Wah mayan tuh ayolah gas kita bayar!.")
print(f"{nama_dua}: Kuy, terimakasi ya bantuannya {nama_satu} setelah ini kuganti uangmu.")
print(f"{nama_satu}: Iya sama sama {nama_dua}, santai aja kaya sama siapa aja.")


print(f"Merekapun pergi ke kasir untuk membayar belian mereka, setelah itu {nama_satu} mengajak {nama_dua} untuk mampir kerumahnya yang tidak jauh dari toko tersebut. {nama_dua} mengiyakan akan mampir setelah mengambil uang di bank.")