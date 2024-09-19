nama="penjual"
nama="pembeli"
harga= 1000

print("Suatu hari ada seorang ibu penjual gorengan, kemudian datanglah pembeli")
stok = input("pembeli : gorengannya masih ada ta bu? ")
sisa = input("pembeli : masih banyak ta bu?")
if stok == "ada" and sisa == "banyak" :
   print("pembeli : berapa satuannya bu?")

print("penjual :", harga)
print("pembeli : eummm oke bu")
print("penjual : jadi mau beli berapa nduk?")
input("pembeli : bakwannya ")
input("tempenya : ")
print("penjual : oke siap")
print("pembeli : totalnya jadi berapa nggih?")

bil1 = int(input("penjual : bakwannya "))
bil2 = int(input("tempenya "))
hasil = bil1+bil2

print("penjual :", bil1, "+", bil2, "totalnya", hasil)
print("pembeli : nggih ini bu uangnya")
print("penjual : makasih nduk")
print("pembeli : nggih sami-sami bu")
