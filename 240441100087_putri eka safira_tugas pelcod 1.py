print("nama = putri eka safira")
print("nim = 240441100087")
print("kelas = C")


#program cerpen : dialog interaktif dengan operasi arotmatika dan operasi logika
print("welcome to my program and enjoyy")
#karakter pertama = edgar
nama_edgar = "edgar"
nilaipjok_edgar = 40
buku_yang_dibawa_edgar = 4

#karakter kedua = sagara
nama_sagara = "sagara"
nilaipjok_sagara = 79
buku_yang_dibawa_sagara = 5

#dialog dimulai
print(f"{nama_sagara} : woi bro gimana hasil ujian lo tadi lancar kaga nih?")
jawaban_edgar = input(f"{nama_edgar} : oit ra, waduh gimana ya kalo ujian sih lancar yang ga lancar nilai ujiannya")
jawaban_sagara =input(f"{nama_sagara}: lancar dong,lo sendiri gimana?lesu banget muka lo")

print(f"{nama_edgar} : gimana kaga lesu,gua dapet nilai 40. lo dapet {nama_sagara}? ")
nilai_pjok_sagara= input(f"{nama_sagara}: gua dapet 79,udah masuk kkm. yang sabar bro,gua saranin lo minta praktek ulang aja")

#menghitung perbedaan nilai
selisih_nilai = abs(nilaipjok_edgar - nilaipjok_sagara)
print(f"{nama_edgar} : saran yang bagus , jadi gua sama lo selisih {selisih_nilai}!")

#menghitung operasi aritmatika untuk menghitung total 
print("OPERASI ARITMATIKA")
total_buku = buku_yang_dibawa_edgar + buku_yang_dibawa_sagara 
print(f"{nama_edgar} : lo kemarin bawa berapa buku paket sagara?soalnya gua dapet info ntar balikin buku total harus 9")
jawaban_sagara = input(f"{nama_sagara} : gua bawa 5 buku,lo sendiri berapa")
jawaban_edgar = input(f"{nama_edgar} : gua bawa 4 buku paket,jadi {total_buku} wih lengkap udah")

print(f"{nama_sagara}: gua mau beli 7 pulpen,satu biji nya seharga rp3500 ")
harga_pulpen = 3500
jumlah_pulpen = 7
total_harga = harga_pulpen * jumlah_pulpen
print(f"{nama_edgar}: jadi total harga pulpen yang lo beli rp{total_harga}")
uang_sagara = int(input(f"{nama_sagara}: gua cuma bawa duit "))


#operasi logika dan memeriksa apakah uangnya cukup?
if uang_sagara >= total_harga:
    print(f"{nama_edgar}: duit lo cukup kaga sag?")
    sisa_uang = uang_sagara - total_harga
    print(f"{nama_sagara}: habis beli pulpen, duit gua sisa Rp{sisa_uang}.")
else:
    kekurangan = total_harga - uang_sagara
    print(f"{nama_edgar}: duit lo kurang Rp{kekurangan}.nih gua pinjemin!")
    print(f"{nama_sagara}: wih terimakasih bantuannya bro")

print(f"TERIMAKASII DAN JUMPA LAGIII")



