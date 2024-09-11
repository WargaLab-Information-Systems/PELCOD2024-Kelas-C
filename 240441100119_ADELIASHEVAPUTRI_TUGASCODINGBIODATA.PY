umuricha = 20
umurreva = 24

print("Selamat datang di percakapan antara Reva dan Icha!")

 # Input nama pengguna
nama1 = input("hallo dengan siapa ini?")
print("hallo" , nama1 , "salam kenal")

print("mari kita baca obrolan reva dan icha")

input("masukkan angka 1 untuk next chapter ")
# Percakapan dimulai
print("Reva: eh haloo icha kita ketemu lagi nihh! oh iya kamu umur berapa sih?")
print("Icha: haloo jugaa Revaa! Umurku" , umuricha , "umurmu berapa rev?")
print("Reva: Aku sii" , umurreva , "tahun.")

 # Operasi aritmatika
selisihumur = umuricha - umurreva
print("Reva: loh ga jauh beda dong, berarti selisih umur kita" , selisihumur , "tahun ya.")

# Input dari pengguna
tebakanumur = int(input(" coba tebak berapa jumlah umur Reva dan Icha: "))

# Operasi aritmatika dan logika
umurkeduanya = umuricha + umurreva

# Output hasil tebakan
if tebakanumur == 44 :
    print("Reva: Wah benar bangett!")
else :
    print("Icha: Maaf yaa, tebakanmu salah. Jumlah umur kami sebenarnya" , umurkeduanya , "tahun.")

input("tekkan angka 1 untuk melanjutkan dialog")

# # Pertanyaan tambahan dengan operasi logika
print("Reva: Hei Icha, aku punya pertanyaan matematika nihh buat kamu.")
Reva_number = 15
Icha_number = 7
    
print("Reva: Jika aku punya" , {Reva_number} , "apel dan kamu punya" , {Icha_number} , "apel, berapa total apel kita?")
    
user_answer = int(input("coba bantu Icha menjawab: "))

hasil = Reva_number + Icha_number

if user_answer == hasil :
        print("Icha: Terimakasih yaa! Jawabannya benar.")
else :
        print("Icha: Hmm, sepertinya itu kurang tepat. Jumlah yang benar adalah" , hasil ,"apel")

# Akhir percakapan
print("Reva: Terima kasih yaa Icha sudah mengobrol")
print("Icha: Sama-sama, Reva. Dan terima kasih juga untuk" , nama1 ," yang sudah berpartisipasi!")