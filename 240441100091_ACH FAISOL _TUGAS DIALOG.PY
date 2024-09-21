nimfaisol=91
nimsheva=119

print("hallo gaes selamat datang dipercakapan antara faisol dan sheva")

#input nama pengguna
nama1=input("Dengan siapa yaa?  ")
print("Halo ",nama1," salam kenal")
print("Selamat datang di percakapan antara faisol dan sheva")
input("ketik next jika ingin memulai percakapan antara faisol dan sheva:")

#memulai percakapan
print("faisol:ehh sheva kita satu kelompok nihh")
print("Sheva :iya sol, kapan mau ngerjain tugasnya? ")
print("faisol:setelah ini")
print("faisol:oh iya btw berapa nimmu?, soalnya mau tak buatin cover buat tugasnya")
print("sheva :kalo nimku ",nimsheva,", kalo nimmu?")
print("faisol:nimku ",nimfaisol,)

#operasi aritmatika
selisihnim = nimfaisol - nimsheva
print("faisol:ga jauh beda ya selisih nim kita, beda ",selisihnim," angka")

#input dari pengguna
tebakannim = int(input("coba kamu tebak berapa jumlahnya kalo nim mereka berdua ditambahkan: "))

#operasi aritmatika dan logika
nimkeduanya = nimfaisol + nimsheva

#hasil tebakan
if tebakannim == 210 :
    print("sheva :bener bangett!, makasih ya sudah bantu menjawab")
else:
    print("faisol: sayang sekali tebakanmu salah:(, jawaban yang benar adalah",nimkeduanya," jumlahnya")
 
input("ketik next jika ingin melanjutkan percakapan mereka berdua:")

#pertanyaan tambahan
print("faisol:eh sheva aku punya pertanyaan nihh")
buah1 = 24
buah2 = 19

print("faisol:misal aku punya apel ",buah1," trus aku kasih ke kamu ",buah2," jadi tinggal berapa buah yang aku punya?")
print("sheva :hmm berapa yaa")
user_unswer = int(input("mari kita bantu sheva menghitung berapa buah apel yang masih tersisa:"))

hasil = buah1 - buah2

if user_unswer == hasil :
    print("sheva :wah terimakasih yaa!! suda bantu menjawab pertanyaannya")
    print("sheva :jawaban kamu benar")
else:
    print("sheva :yahh, kayaknya jawaban kamu salah deh")

#akhir percakapan
print("faisol:terimakasih yaa sheva sudah mau menjawab pertnyaanku")
print("sheva :iya sama-sama faisol. Dan terimakasih juga yaa buat ",nama1,"sudah berpatisipasi di percakapan kita beruda.")