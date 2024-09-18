nama1 = "jihan"
nama2 = "hasan"
nama3 = "ibu kantin"
tahun1 = "2006"
tahun2 = "2005"
angkatan1 = "24"
angkatan2 = "24"

print(f"{nama1}: haii namamu siapa?")
print(f"{nama2}: haii,namaku {nama2}")

print(f"{nama2}: dan siapa nama kamu?")
print(F"{nama1}: kenalin namaku {nama1}")

print(F"{nama1}: kamu kelahiran tahun berapa?")
print(F"{nama2}: aku kelahiran tahun {tahun2}")
print(f"{nama2}: kalau kamu sendiri kelahiran tahun berapa?")
print(F"{nama1}: aku kelahiran tahun {tahun1}")

print(F"{nama1}: kamu angkatan berapa?")
print(F"{nama2}: aku angkatan {angkatan2}")
print(F"{nama2}: berarti kita beda 1 tahun ya?")
print(F"{nama1}: iya beda 1 tahun kita sama diangkatan {angkatan1}")

print(F"{nama2}: ayo kekantin kita sambil ngobrol")
print(F"{nama1}: boleh bolehhh")

print(f"{nama1}: aku mau beli nasi pecel")
print(F"{nama2}: samain aja aku juga nasi pecel")

print(F"{nama2}: berapa harga nasi pecelnya?")
print(F"{nama1}: langsung saja kita tanya harga sekalian pesan nasi pecelnya")
print(F"{nama2}: yaudah ayo")

harganasi1 =int(input(f"{nama1}: berapa harga nasi pecelnya {nama3}"))
harganasi2 =int(input(F"{nama2}: berapa harga nasi pecel satu porsinya {nama3}"))

hasil = harganasi1 + harganasi2

print(F"{nama3}: totalnya", hasil)

harga =str(input(F"{nama1}: harga nasi pecelnya"))
rasa =str(input(F"{nama2}: apa dengan harga segitu rasanya enak?"))
if harga == "murah" and rasa == "enakkk":
    print(F"{nama1}: ayo langsung pesannnn")