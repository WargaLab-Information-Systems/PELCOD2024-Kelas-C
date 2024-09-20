# Karakter pertama: ninda
nama_1 = "ninda"
prodi_2 = "sistem informasi 24"
nilai_kuis1 = 80

nama_2 = "mawar"
prodi_2 = "sistem informasi 24"
nilai_kuis_2 = 75

print(f"{nama_1} : hallo, {nama_2} apa kabar ?")
print(f"{nama_2} : hai,{nama_1}  kabar baik, terima kasih.")

print(f"{nama_1} : oo iya,aku lupa kamu prodi apa ya, {nama_2} ?")
prodi_2 = (input (f"{nama_2} : aku prodi {prodi_2} dan kamu, {nama_1} ?"))
print(f"{nama_1} : ternyata kita satu jurusan dan satu angkatan ya {nama_2} ! ")


print(f"{nama_2} : kalau boleh tahu berapa nilai kuis kamu kemarin ?")
nilai_kuis_1 = float(input(f"{nama_1} : {nilai_kuis1} bagaimana dengan mu, {nama_2}? "))
print(f"{nama_2} : nilai yang bagus ninda")

# Dialog Penutup
print(f"{nama_1} : Semoga kita bisa lebih baik di kuis berikutnya!")
print(f"{nama_2} : Iya, kita harus lebih banyak belajar lagi!")
print(f"{nama_1} : baiklah mawar aku harus pergi sekarang")
print(f"{nama_2} : samapi jumpa lagi ninda")
