# SISTEM PEMESANAN MAKANAN KANTIN TUBES SSEMESTER 1 

# Daftar menu makanan di kantin
menu = [
    ["Nasi Goreng", 15000],
    ["Mie Goreng", 12000],
    ["Ayam Geprek", 18000],
    ["Soto Ayam", 14000],
    ["Es Teh", 5000],
    ["Es Jeruk", 7000],
]

# FUNGSI CREATE

def create(data):
    print("\n=== Tambah Pesanan ===")

    # Input nama pemesan
    nama_pemesan = input("Masukkan nama pemesan: ")

    print("\nMenu Makanan:")
    for i, item in enumerate(menu):
        print(f"{i+1}. {item[0]} - Rp{item[1]}")

    try:
        pilihan = int(input("Pilih menu (nomor): "))
        if pilihan < 1 or pilihan > len(menu):
            print("Menu tidak tersedia!")
            return data
    except ValueError:
        print("Input harus angka!")
        return data

    nama = menu[pilihan-1][0]
    harga = menu[pilihan-1][1]

    try:
        jumlah = int(input("Jumlah pesanan: "))
    except ValueError:
        print("Jumlah harus angka!")
        return data

    total = harga * jumlah
    id_pesanan = len(data) + 1

    # Data: ID, Nama Pemesan, Menu, Harga, Jumlah, Total
    data.append([id_pesanan, nama_pemesan, nama, harga, jumlah, total])
    print("Pesanan berhasil ditambahkan!\n")
    return data

# ALGORITMA SORTING

def bubble_sort(data, index):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j][index] > data[j+1][index]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


# SEARCHING

def search(data, target_id):
    for i in range(len(data)):
        if data[i][0] == target_id:
            return i
    return -1


# FUNGSI READ

def read(data):
    if len(data) == 0:
        print("Belum ada pesanan!")
        return

    print("\n=== Lihat Pesanan ===")
    print("1. Tampilkan semua")
    print("2. Sorting by harga")
    print("3. Sorting by nama menu")
    print("4. Cari berdasarkan ID")

    try:
        pilih = int(input("Pilih menu: "))
    except ValueError:
        print("Input harus angka!")
        return

    if pilih == 1:
        pass

    elif pilih == 2:
        data = bubble_sort(data, 3)
        print("Data berhasil diurutkan berdasarkan harga!")

    elif pilih == 3:
        data = bubble_sort(data, 2)
        print("Data berhasil diurutkan berdasarkan nama menu!")

    elif pilih == 4:
        try:
            id_cari = int(input("Masukkan ID pesanan: "))
        except ValueError:
            print("Input harus angka!")
            return

        idx = search(data, id_cari)
        if idx == -1:
            print("Data tidak ditemukan!")
            return
        else:
            print("\n=== Hasil Pencarian ===")
            print("ID | Nama Pemesan | Menu | Harga | Jumlah | Total")
            d = data[idx]
            print(f"{d[0]} | {d[1]} | {d[2]} | {d[3]} | {d[4]} | {d[5]}")
            return

    print("\n=== DATA PESANAN ===")
    print("ID | Nama Pemesan | Menu | Harga | Jumlah | Total")
    for d in data:
        print(f"{d[0]} | {d[1]} | {d[2]} | {d[3]} | {d[4]} | {d[5]}")
    print()


# FUNGSI UPDATE

def update(data):
    if len(data) == 0:
        print("Belum ada pesanan!")
        return data

    try:
        id_edit = int(input("Masukkan ID pesanan yang akan diedit: "))
    except ValueError:
        print("Input harus angka!")
        return data

    idx = search(data, id_edit)
    if idx == -1:
        print("Data tidak ditemukan!")
        return data

    print("\nPesanan ditemukan!")
    print(f"Nama Pemesan: {data[idx][1]}")
    print(f"Menu: {data[idx][2]}")
    print(f"Harga: {data[idx][3]}")
    print(f"Jumlah: {data[idx][4]}")

    try:
        jumlah_baru = int(input("Masukkan jumlah baru: "))
    except ValueError:
        print("Jumlah harus angka!")
        return data

    data[idx][4] = jumlah_baru
    data[idx][5] = data[idx][3] * jumlah_baru

    print("Pesanan berhasil diupdate!\n")
    return data


# FUNGSI DELETE

def delete(data):
    if len(data) == 0:
        print("Belum ada pesanan!")
        return data

    try:
        id_hapus = int(input("Masukkan ID pesanan yang akan dihapus: "))
    except ValueError:
        print("Input harus angka!")
        return data

    idx = search(data, id_hapus)
    if idx == -1:
        print("Data tidak ditemukan!")
        return data

    data.pop(idx)
    print("Pesanan berhasil dihapus!\n")
    return data


# MENU UTAMA

def menuUtama():
    print("===================================")
    print("=== Sistem Pemesanan Kantin ===")
    print("===================================")
    print("1. Tambah Pesanan")
    print("2. Lihat Pesanan")
    print("3. Edit Pesanan")
    print("4. Hapus Pesanan")
    print("5. Keluar")

    try:
        pilihan = int(input("Masukkan pilihan [1 - 5]: "))
        if pilihan < 1 or pilihan > 5:
            print("Pilihan tidak valid!")
            return 0
        return pilihan
    except ValueError:
        print("Input harus angka!")
        return 0


# PROGRAM UTAMA

pilihan = 0
data = []

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

print("Terima kasih telah menggunakan sistem!")
