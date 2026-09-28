
#KALKULATOR

print("== KALKULATOR PENGELUARAN ==")

uang = int(input("Masukkan uang yang kamu punya: "))

total_pengeluaran = 0

while True:
    nama = input("\nApa yang di beli? (ketik sudah untuk menghitung pengeluaran): ")

    if nama.lower() == "sudah":
        break

    harga = int(input("Masukkan harga: "))

    total_pengeluaran = total_pengeluaran + harga

    print(nama, "=", harga)
    print("Total pengeluaran =", total_pengeluaran)

sisa = uang - total_pengeluaran

print("\n== HASIL ==")
print("Uang awal =", uang)
print("Total pengeluaran =", total_pengeluaran)
print("Sisa uang =", sisa)

if sisa > 0:
    print("Uang masih tersisa")
elif sisa == 0:
    print("Uang habis")
else:
    print("Pengeluaran melebihi uang")



# PENGULANGAN

    # POLA KOTAK

print("== KOTAK ==")

ukuran = int(input("Masukkan ukuran kotak: "))

for i in range(ukuran):
    for j in range(ukuran):
        print("*", end=" ")
    print()


#  POLA SEGITIGA 

print("\n== SEGITIGA ==")

tinggi = int(input("Masukkan tinggi segitiga: "))

for i in range(1, tinggi + 1):
    for j in range(i):
        print("*", end=" ")
    print()


#  POLA PERSEGI PANJANG 

print("\n== PERSEGI PANJANG ==")

panjang = int(input("Masukkan panjang: "))
lebar = int(input("Masukkan lebar: "))

for i in range(lebar):
    for j in range(panjang):
        print("*", end=" ")
    print()