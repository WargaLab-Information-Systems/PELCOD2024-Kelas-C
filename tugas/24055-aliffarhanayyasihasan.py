nama1 = "upin"
nama2 = "ipin"

print(f"{nama1} :halo bro,{nama2} Gimana sekolahnya lancar?")
print(f"{nama2} :oii, lumayan capek  bro")
print(f"{nama1} :biar gak capek ayo kita main tebak tebakkan, gimana mau?")
print(f"{nama2} :boleh apa pertanyaannya?")
print(f"{nama1} :Rina memiliki 4 kantung berisi permen. Jika setiap kantung berisi 8 permen, maka berapa jumlah permen yang dimiliki Rina?")
print(f"{nama2} :ehh berapa yaa....")
print(f"{nama1} :hayo berapa hayooo")
jawaban = int(input(f"{nama2} :"))

hasil = 4 * 8 
if hasil == jawaban:
    print(f"{nama1} :iya jawabanmu benar")
    print(f"{nama2} :asekk jawabannku benar")
else:
    print(f"{nama1} : jawabanmu salah")
    print(f"{nama2} :iya aku ga bisa")

    print(f"{nama1} :yaudah nanti aku ajarin")
    print(f"{nama2} :okelah terimakasih")