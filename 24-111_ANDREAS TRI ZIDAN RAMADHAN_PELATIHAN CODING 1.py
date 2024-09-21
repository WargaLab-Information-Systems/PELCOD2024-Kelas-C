ukuransepaturusdi = 40
ukuransepatuzidan = 42

print("Selamat datang di percakapan antara zidan dan rusdi!")

 # Input nama pengguna
nama1 = input("Hai dengan siapa ini?")
print("Hai" , nama1 , "salam kenal")

print("mari kita baca obrolan zidan dan rusdi")

input("masukkan kata GO untuk next chapter ")
# Percakapan dimulai
print("zidan: haloo rusdi kita ketemu lagi, sepatumu bagus tuh berapa ukurannya?")
print("rusdi: haloo jugaa zidan! Umurku" , ukuransepaturusdi , "ukuran sepatumu berapa dan?")
print("zidan: punyaku ukuran" , ukuransepatuzidan , )

#  Operasi aritmatika
selisihukuran = ukuransepaturusdi - ukuransepatuzidan
print("zidan: loh ga jauh beda dong, berarti ukuran sepatu kita" , selisihukuran , "ya.")

# Input dari pengguna
tebakanukuran = int(input(" coba tebak berapa jumlah ukuran sepatu zidan dan rusdi: "))

# Operasi aritmatika dan logika
ukurankeduanya = ukuransepaturusdi + ukuransepatuzidan

# Output hasil tebakan
if tebakanukuran == 82 :
    print("zidan: Wah benar bangett!")
else :
    print("rusdi: Maaf yaa, tebakanmu salah. Jumlah umur kami sebenarnya" , ukurankeduanya ,)

input("masukkan kata GO untuk melanjutkan dialog")

# # Pertanyaan tambahan dengan operasi logika
print("zidan: Hei rusdi, aku punya pertanyaan matematika nihh buat kamu.")
zidan_number = 16
rusdi_number = 11
    
print("zidan: Jika aku punya" , {zidan_number} , "anggur dan kamu punya" , {rusdi_number} , "anggur, berapa total anggur kita?")
    
user_answer = int(input("coba bantu rusdi menjawab: "))

hasil = zidan_number + rusdi_number

if user_answer == hasil :
        print("rusdi: Terimakasih yaa! Jawabannya benar.")
else :
        print("rusdi: Hmm, sepertinya itu kurang tepat. Jumlah yang benar adalah" , hasil ,"anggur")

# Akhir percakapan
print("zidan: Terima kasih yaa rusdi sudah mengobrol")
print("rusdi: Sama-sama, zidan. Dan terima kasih juga untuk" , nama1 ," yang sudah berpartisipasi!")
