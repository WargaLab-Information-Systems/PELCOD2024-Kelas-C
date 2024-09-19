nama1 = input("Masukkan nama orang pertama: ")
nama2 = input("Masukkan nama orang kedua: ")
umur1 = 18
umur2 = 20

print(f"\n{nama1}: Hai {nama2}, Salam kenal ya aku {nama1}, kalo kau, siapa namamu?")
print(f"{nama2}: Hai juga {nama1}, nama aku {nama2}, salam kenal ya")
print(f"{nama1}: Oke salam kenal, btw orang mananya kau?")
print(f"{nama2}: Aku dari Medan, tepatnya di Berastagi")
print(f"{nama1}: Asik, samanya kita dari Medan, kalo aku dari kabanjahe")
print(f"{nama2}: Kebetulan kali kita bertemu disini ya haha")

print(f"\n{nama1}: Btw, Berapa umurmu {nama2}?")
print(f"{nama2}: Umurku {umur2}, kalo kau?")
print(f"{nama1}: Kalo umurku {umur1}.")
print(f"{nama2}: Selisih berapa tahun kita ini?")

selisih_umur = abs(umur1 - umur2)

print(f"\n{nama1}: Ayo kita hitung selisih umur kita!.")
print(f"{nama2}: Hmm, berapa ya?")
print(f"{nama1}: Selisih umur kita adalah {selisih_umur} tahun.")

print(f"\n{nama2}: Oiya, Aku suka kali loh sama matematika . Maunya kau bermain tebak-tebakan?")
print(f"{nama1}: Ayo lah, tebak-tebakan kita!")

angka1 = 15
angka2 = 7
hasil = angka1 + angka2

print(f"{nama2}: Berapa hasil dari {angka1} + {angka2}?")
jawaban_nama1 = int(input(f"{nama2}: Menurutku hasilnya "))

if jawaban_nama1 == hasil:
    print(f"{nama2}: Benar sekali! haha Kamu pintar matematika.")
else:
    print(f"{nama2}: Maaf, jawabanmu kurang tepat loh. Hasil yang benar itu {hasil}.")

print(f"{nama1}: Haha okelah, senang berjumpa denganmu,{nama2}!")
print(f"{nama2}: Oke, {nama1}. Senang bisa berjumpa denganmu disini!")