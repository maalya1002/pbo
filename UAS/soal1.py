KatMHS = [
    {"id": 1,"nama": "Berprestasi", "total": 4000000, "potongan": 0.08},
    {"id": 2,"nama": "KIP", "total": 3000000, "potongan": 0.05},
    {"id": 3,"nama": "Non beasiswa", "total": 5000000, "potongan": 0}
]


def totalspp(kategori):
    for data in KatMHS:
        if data["id"] == kategori:
            bayar = data["total"] - (data["total"] * data["potongan"])
            print("Total pembayaran SPP untuk kategori", kategori, ": Rp", bayar)
            break
    else:
        print("kategori tidak terdaftar dalam program.")


kategori = input("Masukkan kategori mahasiswa\n1.Berprestasi\n2.KIP\n3.Non Beasiswa\n: ")

totalspp(int(kategori))
