print("dialog dari karina dan giselle")
input("tekan enter untuk ke dialog ")
karakter1 = "karina"
karakter2 = "giselle"

print(f"{karakter1}: Hai {karakter2}, Kamu abis dari mana kok kayak buru-buru gitu?")
print(f"{karakter2}: Halo {karakter1}, Iya nih aku lagi buru-buru, soalnya laptopku ketinggalan dikos.")

print(f"{karakter1}: Oh gitu, pantes kok buru-buru. Emang sekarang kamu matkul apa?")
print(f"{karakter2}: Biasaa, Matkul Algoritma Pemograman")

print(f"{karakter1}: Ohh matkul yang susah itu ya")
print(f"{karakter2}: Yaps, bener.")

print(f"{karakter1}: Semangat deh")
print(f"{karakter1}: Mampir dulu ke toko beli minum, kamu kayak kecapekan gitu")

print(f"{karakter2}: Iya deh aku beli minum dulu")
print(f"{karakter2}: kira-kira berapa ya harga minumnya?")

print(f"{karakter1}: Tanya dulu yuk harganya")
print(f"{karakter2}: Iya ayok")

print(f"{karakter2}:  Makasih banyak ya tawarannya. Yaudah aku duluan ya, takut telat")
print(f"{karakter1}: Iya, Hati-hati dijalan")

hargaminuman1 =int(input(f"{karakter1}: Berapa harga minumnya buk."))
hargaminuman2 =int(input(f"{karakter2}: Berapa harga minumnya buk."))

hasil = hargaminuman1 + hargaminuman2

print("penjagatoko : totalnya", hasil)

Harga =str(input(f"{karakter1}: Berapa harganya"))
Rasa =str(input(f"{karakter2}: Gimana rasanya?"))
if Harga =="murah" and Rasa =="seger":
    print(f"{karakter2}: Ayok belii")