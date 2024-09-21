#Mendefinisikan sebuah karakter/Nama Orang
Orang1="Ayu"
Orang2="Desi"

#Percakapan Pertama
print(f"{Orang1} : Hai, {Orang2} Apa Kabar, Sehat Nih? ")
print(f"{Orang2} : Iya Halo {Orang1} Sehat-sehat aja nih, Kalau kamu Sehat Ngak Nih?")

print(f"{Orang1} : Alhamdulillah Untuk saat ini masih sehat!")
print(f"{Orang1} : Oh iya {Orang2} tugas pelcod kemarin kamu udah atau belum ? (Udah/Belum) : ")
Jawaban=input(f"{Orang2} : ")

if Jawaban.lower() == "udah":
    print(f"{Orang2} : Udah dong orang tugas gampang gitu aja kok")
else:
    print(f"{Orang2} : Belum nih, Aku masih pusing karena ga bisa Coding")

print(f"{Orang1} : Lah Sama dong wkwkwk")
print(f"{Orang1} : Eh btw umur kamu sekarang itu berapa tahun sih?")

#Input untuk mendapatkan data usia Ayu=int(input(f"{Orang2} : Umur Aku sekarang Masih (Masukkan Angka Saja) : "))
usia_Desi=int(input(f"{Orang1} : Kalau umur aku sekarang sudah (Masukkan Angka Saja) : "))

#Menghitung jumlah Perbedaan Usia
Perbedaan_usia =abs(usia_Ayu - usia_Desi)

# Penyeleksian kondisi operasi logika untuk perbandingan umur
if usia_Ayu>usia_Desi:
    print(f"{Orang1} : Eh ternyata aku lebih tua {Perbedaan_usia} tahun dari kamu")
elif usia_Ayu<usia_Desi:
    print(f"{Orang1} : Eh ternyata aku lebih muda {Perbedaan_usia} tahun dari kamu")
else:

# Lanjut dengan operasi aritmatika lain
Total_usia = usia_Ayu + usia_Desi 
print(f"{Orang2} : Kira-Kira usia kita berdua kalau di tambahkan jadi berapa ya?")
print(f"{Orang1} : Bentar Mikir!")
print(f"{Orang1} : Umurku kan {usia_Ayu} tahun + Usia kamu {usia_Desi} tahun jadi Totalnya")
print(f"{Orang1} : {Total_usia} tahun dong")

print(f"{Orang2} : Ternyata kamu bisa berhitung juga ya mas wkwkwkwk")
print(f"{Orang1} : Orang ini aja pakai Kalkulator")
print(f"{Orang2} : owalah pantes bisa cepet gitu ya ternyata pake kalkulator")
print(f"{Orang1} : iya hehehe aku lemot soal kalau mikir")
