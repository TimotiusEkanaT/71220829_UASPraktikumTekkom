print("==== Selamat datang di XXV ====")
upilkuda=int(input("Masukkan tanggal hari ini: "))

print ("== Berikut genre film yang tersedia ==")
print ("1. Horor")
print ("2. Action")

taikayam=input("Silahkan pilih mau nonton film berfenre apa :")
if taikayam == ("1","2"):
    print (" ")
    print ("== Berikut pilihan film yang sedang tanyang ==")
    print ("1. Black Phanter: Wakanda Forever")
    print ("2. Avatar: The Way of Water")
    print ("")
    input ("Silahkan pilih mau nonton film apa : ")
else:
    print("Pilihan anda tidak tersedia di bioskop ini")

nakkakros=int(input("Mau memesan tiket sebanyak :"))
if upilkuda%2==0:
    print ("Total yang harus dibayar adalah", nakkakros*25000*2/100)
else:
    print ("Total yang harus dibayar adalah Rp.", nakkakros*25000)
