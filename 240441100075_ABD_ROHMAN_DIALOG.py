nama1 = "Rohman" 
nama2 = "Imam"
tinggi1 = 160
tinggi2 = 165

print(f"{nama1}: bro, bagaimana kabarmu?")
print(f"{nama2}: alhamdulillah bro baik")
print(f"{nama1}: wihhh, tinggi banget kau sekarang yaaa")
print(f"{nama2}: iya lahh bro, aku rajin olahraga soalnya")
print(f"{nama1}: emang berapa sih tinggi mu?")
print(f"{nama2}: kamaren sihh aku ngukur {tinggi2}")
print(f"{nama1}: kalo aku sih masi {tinggi1} anjayyy ")

selisih_tinggi = tinggi2 - tinggi1

print(f"\n{nama1}: coba deh kita hitung tinggi badan kita")
print(f"{nama2}: coba aku itung dulu iyaaa")
print(f"{nama2}: kalo di itung-itung sih kagak beda jauh anjayyy")
print(f"{nama1}: emangnya berapa sihhh?")
print(f"{nama2}: jadi tinggi badan kita tuhh cuma selisih {selisih_tinggi} cm")

response =  input(f"{nama2}: kamu mau gak cara tips naikin tinggi badan? (iya/tidak): ").lower()

if response == "iya":
    print("jadi gini cara tips naikin tinggi badan:\n1. rajin olahraga.\n2. makanan  yang bergizi.\n3. tidur yang cukup.")
elif response == "tidak":
    print("yaudah kalo engga mau, lain kali kabari aku aja ya kalo butuh tips.")
else: 
    print(f"input tidak valid, silahkan jawab dengan 'iya' atau 'tidak'.")

print(f"\n{nama1}: oke siap terimakasih banyak atas waktunya, sampai jumpa")
print(f"{nama2}: oke siap sama-sama bro")

