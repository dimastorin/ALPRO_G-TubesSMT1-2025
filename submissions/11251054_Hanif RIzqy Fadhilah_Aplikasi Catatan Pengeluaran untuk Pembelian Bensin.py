import datetime

def create(data):
    while True:
        tggl_input = input("Masukkan tanggal beli bensin dengan format (YYYY-MM-DD): ")
        try:
            tanggal = datetime.datetime.strptime(tggl_input, "%Y-%m-%d")
            tanggal = tanggal.date()
            break
        except ValueError:
            print("Format tanggal salah! Gunakan format YYYY-MM-DD")

    try:
        pengeluaran = int(input("Masukkan nominal uang yang dikeluarkan untuk bensin: "))
        if pengeluaran <= 0:
            print("Nominal harus lebih dari nol!")
            return data
    except ValueError:
        print("Program hanya menerima input nominal berupa angka!")
        return data

    data.append([str(tanggal), pengeluaran])
    print("Data berhasil ditambahkan!")
    return data

def read(data):
    if len(data) == 0:
        print("Belum ada data pengeluaran")
    else:
        print(f"{'Tanggal':<15} {'Pengeluaran (Rp)':>20}")
        print("-" * 35)
        for Data in data:
            print(f"{Data[0]:<15} {Data[1]:>20,}")
        print("-" * 35)

def update(data):
    if len(data) == 0:
        print("Tidak ada data yang bisa di ubah")
        return data
    
    while True:
        tggl_input2 = input("Masukkan tanggal dari data yang ingin di ubah (YYYY-MM-DD): ")
        try:
            tggl = datetime.datetime.strptime(tggl_input2, "%Y-%m-%d").date()
            tggl_input2 = str(tggl)
            break
        except ValueError:
            print("Format tanggal salah! Gunakan format YYYY-MM-DD")

    for Data in data:
        if Data[0] == tggl_input2:
            try:
                ubah = int(input("Masukkan nominal baru: "))
                if ubah <= 0:
                    print("Nominal harus lebih dari 0")
                    return data
                Data[1] = ubah
                print("Data berhasil di update!")
                return data
            except ValueError:
                print("Input harus berupa angka!")
                return data

    print("Data tidak ditemukan")
    return data

def delete(data):
    if len(data) == 0:
        print("Tidak ada data yang bisa dihapus!")
        return data

    hapus_tgl = input("Masukkan tanggal data yang ingin dihapus (YYYY-MM-DD): ")

    try:
        tgl = datetime.datetime.strptime(hapus_tgl, "%Y-%m-%d").date()
        hapus_tgl = str(tgl)
    except ValueError:
        print("Format tanggal salah!")
        return data

    for Data in data:
        if Data[0] == hapus_tgl:
            data.remove(Data)
            print("Data berhasil dihapus!")
            return data

    print("Data tidak ditemukan!")
    return data


def search(data):
    if len(data) == 0:
        print("Tidak ada data untuk dicari!")
        return

    katakunci = input("Masukkan tanggal yang ingin dicari dengan format (YYYY-MM-DD): ")

    ditemukan = False
    for Data in data:
        if Data[0] == katakunci:
            print("Data ditemukan:")
            print(f"Tanggal: {Data[0]}")
            print(f"Pengeluaran: Rp {Data[1]:,}")
            ditemukan = True

    if not ditemukan:
        print("Data tidak ditemukan")

def sorting(data):
    if len(data) == 0:
        print("Tidak ada data untuk diurutkan!")
        return data

    print("Pilih metode sorting:")
    print("1. Pengeluaran terbesar (Descending)")
    print("2. Pengeluaran terkecil (Ascending)")

    try:
        pilih = int(input("Masukkan pilihan: "))

        if pilih == 1:
            for i in range(len(data)):
                for j in range(len(data) - i - 1):
                    if data[j][1] < data[j+1][1]:
                        temp = data[j+1]
                        data[j+1] = data[j]
                        data[j] = temp
            print("Data setelah diurutkan (Descending):")

        elif pilih == 2:
            for i in range(len(data)):
                for j in range(len(data) - i - 1):
                    if data[j][1] > data[j+1][1]:
                        temp = data[j+1]
                        data[j+1] = data[j]
                        data[j] = temp
            print("Data setelah diurutkan (Ascending):")

        else:
            print("Pilihan tidak valid.")
            return data

    except ValueError:
        print("Input harus angka!")
        return data

    print(f"{'Tanggal':<15} {'Pengeluaran (Rp)':>20}")
    print("-" * 35)
    for d in data:
        print(f"{str(d[0]):<15} {d[1]:>20,}")
    print("-" * 35)

    return data

    



def menuUtama():
    print("====================================")
    print("=== Aplikasi Catatan Pengeluaran ===")
    print("===    untuk Pembelian Bensin    ===")
    print("===        by Hanif 1154         ===")
    print("====================================")
    print("1. Tambah Pengeluaran")
    print("2. Lihat Semua Pengeluaran")
    print("3. Edit Pengeluaran")
    print("4. Hapus Data Pengeluaran")
    print("5. Cari Data (Search)")
    print("6. Sorting Pengeluaran")
    print("7. Keluar")
    try:
        pilihan = int(input("Masukkan pilihan [1 - 7]: "))
        if pilihan < 1 or pilihan > 7:
            print("Pilihan hanya antara 1 sampai 7. Silakan coba lagi.")
        else:
            return pilihan
    except ValueError:
        print("Input harus berupa angka.")



##### PROGRAM UTAMA #####

pilihan = 0
data = []

while pilihan != 7:
    pilihan = menuUtama()
    if pilihan == 1:
        data = create(data)
    elif pilihan == 2:
        read(data)
        input("Kembali tekan ENTER..")
    elif pilihan == 3:
        data = update(data)
    elif pilihan == 4:
        data = delete(data)
    elif pilihan == 5:
        search(data)
        input("Kembali tekan ENTER..")
    elif pilihan == 6:
        data = sorting(data)
        input("Kembali tekan ENTER..")

print("Terima kasih..!")