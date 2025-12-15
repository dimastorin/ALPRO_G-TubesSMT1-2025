#data awal
def buku_tersedia():
    return [
        {"judul": "Negeri Di Ujung Tanduk", "penulis":  "Tere Liye", "tahun": "2013"},
        {"judul": "Funiculi Funicula", "penulis":  "Toshikazu Kawaguchi", "tahun": "2015"},
        {"judul": "Si Anak Spesial", "penulis":  "Tere Liye", "tahun": "2018"},
    ]

#buat nambah data
def create(data):
    print("=== Tambah Buku Baru ===")
    while True:
        judul = input("Masukkan judul buku: ").strip()
        if judul != "":
            break
        else:
            print("Judul harus terisi.")  
    while True:
        penulis = input("Masukkan nama penulis: ").strip()
        if penulis.replace(" ", "").isalpha():  
            break
        else:
            print("Nama penulis harus huruf.")
    while True:
        tahun = input("Masukkan tahun terbit: ")
        try:
            int(tahun)
            break
        except:
            print("Tahun harus angka.")
    buku = {"judul": judul, "penulis": penulis, "tahun": tahun}
    data.append(buku)
    print("Buku berhasil ditambahkan!")

#lihat buku
def read(data):
    print("=== Daftar Buku Bacaan ===")
    print("1. Tampilkan semua (urut berdasarkan judul)")
    print("2. Cari buku berdasarkan judul")
    while True:
        try:
            pilih = int(input("Pilih (1-2): "))
            if pilih in [1, 2]:
                break
            else:
                print("Pilihan hanya 1 atau 2.")
        except:
            print("Input harus angka.")
    if pilih == 1:
        data_sorted = sorted(data, key=lambda x: x["judul"])
        for i, buku in enumerate(data_sorted):
            print(f"{i+1}. {buku['judul']} - {buku['penulis']} ({buku['tahun']})")
    elif pilih == 2:
        cari = input("Masukkan judul yang dicari: ")
        ditemukan = False
        for buku in data:
            if cari.lower() in buku["judul"].lower():
                print(f"{buku['judul']} - {buku['penulis']} ({buku['tahun']})")
                ditemukan = True
        if not ditemukan:
            print("Buku tidak ditemukan.")
    else:
        print("Pilihan tidak valid.")

#edit buku
def update(data):
    print("=== Edit Buku ===")
    for i, buku in enumerate(data):
        print(f"{i+1}. {buku['judul']} - {buku['penulis']} ({buku['tahun']})")
    try:
        idx = int(input("Pilih nomor buku yang diedit: ")) - 1
        if 0 <= idx < len(data):
            print("Kosongkan jika tidak ingin mengubah.")
            judul = input(f"Judul baru ({data[idx]['judul']}): ") or data[idx]['judul']
            penulis = input(f"Penulis baru ({data[idx]['penulis']}): ") or data[idx]['penulis']
            tahun = input(f"Tahun baru ({data[idx]['tahun']}): ") or data[idx]['tahun']
            data[idx] = {"judul": judul, "penulis": penulis, "tahun": tahun}
            print("Data buku berhasil diperbarui!\n")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus angka.")
    return data

#hapus buku
def delete(data):
    print("=== Hapus Buku ===")
    for i, buku in enumerate(data):
        print(f"{i+1}. {buku['judul']} - {buku['penulis']} ({buku['tahun']})")
    try:
        idx = int(input("Masukkan nomor buku: ")) - 1
        if 0 <= idx < len(data):
            del data[idx]
            print("Data dihapus.")
        else:
            print("Nomor tidak tersedia.")
    except ValueError:
        print("Masukkan angka.")
    return data

#tampilan
def menuUtama():
    print("===================================")
    print("===     Daftar Buku Bacaan      ===")
    print("===         by Evi J.           ===")
    print("===================================")
    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Edit Buku")
    print("4. Hapus Buku")
    print("5. Keluar")
    try:
        pilihan = int(input("Masukkan pilihan (1-5): "))
        if pilihan < 1 or pilihan > 5:
            print("Pilihan hanya 1-5")
            return 0
        return pilihan
    except ValueError:
        print("Masukkan Angka")
        return 0

#Program Utama
data = buku_tersedia()
pilihan = 0
while pilihan != 5:
    pilihan = menuUtama()
    if pilihan == 1:
        data = create(data)
    elif pilihan == 2:
        read(data)
        input("Tekan ENTER untuk kembali...")
    elif pilihan == 3:
        data = update(data)
    elif pilihan == 4:
        data = delete(data)
print("Program selesai.")

