# Inisialisasi variabel
reva_age = ()
prama_age = ()

# Fungsi untuk mendapatkan input pengguna
def get_user_input(prompt):
    return input(prompt)

# Mulai percakapan
print("prama: Halo reva! Berapa umurmu sekarang?")
reva_age = int(get_user_input("reva: Umurku "))

print(f"reva: Umurku {reva_age} tahun. Kalau kamu prama?")
prama_age = int(get_user_input("prama: Aku berumur "))

# Operasi aritmatika
prama_difference = abs(reva_age - prama_age)

print(f"prama: Wah, selisih umur kita {prama_difference} tahun!")

# Operasi logika
if reva_age > prama_age:
    print("reva: Iya, aku lebih tua darimu.")
elif reva_age < prama_age:
    print("reva: Ternyata kamu lebih tua dariku.")
else:
    print("reva: Wah, ternyata umur kita sama!")

# Input pengguna untuk hobi
prama_hobby = get_user_input("prama: Ngomong-ngomong, apa hobimu, Reva? ")
print(f"reva: Oh, hobiku adalah {prama_hobby}. Kalau kamu?")
reva_hobby = get_user_input("prama: Hobiku ")

# Operasi logika untuk membandingkan hobi
if prama_hobby.lower() == reva_hobby.lower():
    print("reva: Wah, hobi kita sama!")
else:
    print("reva: Menarik juga hobi kita berbeda.")

# Operasi aritmatika dengan input pengguna
print("prama: Hei, ayo main tebak-tebakan matematika!")
number1 = int(get_user_input("prama: Berapa 10 x 7? "))
correct_answer = 10 * 7

if number1 == correct_answer:
    print("reva: Benar sekali! Kamu pintar matematika ya.")
else:
    print(f"reva: Hmm, sebenarnya jawabannya adalah {correct_answer}.")

print("prama: Terima kasih Reva, senang ngobrol denganmu!")
print("reva: Sama-sama prama, sampai jumpa!")