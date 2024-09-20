harga_tiket = 50000  
uang_tamara = 120000   
uang_nopa = 70000    


print("tamara: Hai nop, apa kabar?")
print("nopa: Hai tam, kabar baik! kamu gimana??")
print("tamara: Aku juga baik, terima kasih! Aku dengar ada film baru yang bagus. Mau nonton bareng ga? di bioskop?")

# respon
jawaban_tamara= input("nopa: (Ketik 'ya' atau 'tidak') ").strip().lower()


if jawaban_tamara == "ya":
    print("\ntamara: Bagus! Berapa tiket yang ingin kamu beli, nopa?")
    tiket_nopa = int(input("nopa: Saya ingin membeli "))  # nopa memasukkan jumlah tiket yang ingin dibeli
    
    print("\ntamara: Oke, aku juga ingin beli tiket.ya")
    tiket_tamara = int(input("tamara: Aku akan membeli "))  # tamara memasukkan jumlah tiket yang ingin dibeli
    
    
    total_tiket = tiket_nopa + tiket_tamara
    total_harga = total_tiket * harga_tiket
    print(f"\ntamara: Jadi, kita akan membeli {total_tiket} tiket dengan total harga Rp {total_harga:,}.")

    
    total_uang = uang_tamara + uang_nopa
    print(f"tamara: Jika kita gabungkan, uang kita menjadi Rp {total_uang:,}.")

    
    if total_uang >= total_harga:
        sisa_uang = total_uang - total_harga
        print(f"nopa: Kita cukup uang! Setelah membeli tiket, kita masih punya sisa Rp {sisa_uang:,}.")
    else:
        kekurangan = total_harga - total_uang
        print(f"nopa: Sepertinya uang kita tidak cukup. Kita kekurangan Rp {kekurangan:,}.")
        
        
        kurangi_tiket = input("tamara: Apakah kamu ingin mengurangi jumlah tiket? (ya/tidak) ").strip().lower()
        if kurangi_tiket == "ya":
            tiket_kurang = int(input("nopa: Berapa tiket yang ingin kamu kurangi? "))
            tiket_nopa -= tiket_kurang
            total_tiket = tiket_nopa + tiket_tamara
            total_harga = total_tiket * harga_tiket
            print(f"\nRina: Sekarang kita akan membeli {total_tiket} tiket dengan total harga Rp {total_harga:,}.")
            
            if total_uang >= total_harga:
                sisa_uang = total_uang - total_harga
                print(f"nopa: Sekarang uang kita cukup! Setelah membeli tiket, kita masih punya sisa Rp {sisa_uang:,}.")
            else:
                kekurangan = total_harga - total_uang
                print(f"nopa: Meskipun sudah dikurangi, kita masih kekurangan Rp {kekurangan:,}. Mungkin kita bisa ajak teman lain untuk nonton bareng.")
        else:
            print("\nnopa: Oke, mungkin kita bisa beli tiket lain kali.")

else:
    print("\ntamara: Tidak masalah, mungkin lain kali kita bisa nonton bersama.")


print("\ntamara: okke see you, nop!")
print("nopa: see you tamm!")
