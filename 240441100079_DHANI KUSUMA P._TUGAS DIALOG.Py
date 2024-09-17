rint("disuatu jam selesai matkul ada dua orang maba yang bertemu mereka saling berkenalan dan saling menyapa")

nama1 = "kusuma"
nama2 = input("masukkan nama anda untukk berdialog dengan kusuma ")
alamat1 = "lamongan"
angkatan1 = 24


print("kusuma : hai boleh kenalan, siapa namamu?")
print(nama2 ,": 0h hallo, boleh dong, namaku" , nama2)
print(nama2 , ": dan siapa namamu?")
print("kusuma : namaku", nama1)

input("enter untuk next dialog")

print("kusuma : eh kamu alamatnya dimana?")
alamat2 = input("masukkan alamat anda ")
print( nama2 , ": aku berasal dari" , alamat2)

input("enter untuk next dialog")

print(nama2 , ": emmm, kamu alamatnya dimana? ")
print("kusuma : aku berasal dari" ,alamat1)

if alamat2 == "lamongan" : 
    print("kusuma : loh sama sama lamongan ya.. hehe")
else :
    print( "kusuma : ohh kamu dari" ,alamat2 , "ya !!!!")

input("enter untuk next dialog")

print("kusuma : eh", nama2 , "em kamu angkatan berapa ya ")
angkatan2 = input("masukkan angkatan anda ")
print(nama2 , ": aku angkatan ", angkatan2)

input("enter untuk next dialog")

print(nama2 , ": lah kalo kamu kusuma, angkatan berapa? ")
print("kusuma : aku ", angkatan1)

input("enter untuk next dialog")

print("kusuma : eh kok cuaca nya panas, ayo ke kantin buat beli es? ")

dhani = input("masukkan jawaban? ")

if dhani =="ayo" :
    print(nama2 , " : gaskeun ke kantin") 
else :
    print("kusuma : langsung aja kekantin boy")

print("akhirnya mereka ke kantin untuk berteduh dan makan")

input("enter untuk next dialog")

print("selesai makan mereka ingin membayar ke ibu kantin dan mereka berencana membayar menjadi satu")
print("mereka pun berdialog")

input("enter untuk next dialog")

uang1 = 5000
uang2 = 7500
print("dhani : eh uangmu ada berapa?")
print("kusuma : uangku ada" , uang1 , "lah uangmu berapa?")
print("dhani : uangku ada" , uang2 , "ini jadi satu totalnya berapa?")

money = input("kusuma : bentar tak itung dulu ")

if money == "oke":
    print("kusuma : " , uang1 , " ditambah " , uang2 , "kan")
else :
    print(" kusuma : beraapa y..?")

print("TOLONG BANTU KUSUMA DALAM MENGHITUNG")
    
bil1uangkusuma = int(input("masukkan uang kusuma :"))
bil2uangdhani = int(input("masukkan uang dhani :") )

hasil = bil1uangkusuma + bil2uangdhani 

print("hasil penjumlahan dari uang kusuma sebesar" , bil1uangkusuma , "ditambah uang" , nama2 , "sebesar" , bil2uangdhani , "adalah" , hasil)

print("akhirnya mereka berdua mebayar uang sebesar" , hasil , "ke ibu kantin dan mereka pulang")

input("enter untuk next dialog")

print("selesaiiiiii")
