import sys
# Data Kendaraan 
data_kendaraan = [
    {"id": "M001", "merk": "Honda Beat", "warna": "Merah", "harga_sewa": 50000, "status": "Tersedia"},
    {"id": "M002", "merk": "Yamaha NMAX", "warna": "Hitam", "harga_sewa": 80000, "status": "Disewa"},
    {"id": "M002", "merk": "Honda Vario", "warna": "Putih", "harga_sewa": 75000, "status": "Tersedia"},
]
def jeda():
    input("\nTekan ENTER untuk melanjutkan...")

def cari_index_data(data_list, target_id):
    for i, kendaraan in enumerate(data_list):
        if kendaraan['id'].upper() == target_id.upper():
            return i
    return -1

def tampilkan_data(data_list):
    print("\n--- Daftar Kendaraan ---")
    if not data_list:
        print("Data kendaraan kosong.")
        return
    print(f"{'No.':<4}{'ID':<6}{'Merk':<15}{'Warna':<10}{'Harga Sewa':<15}{'Status':<10}")
    print("-" * 65)
    for i, k in enumerate(data_list):
        harga_format = f"Rp {k['harga_sewa']:,}" 
        print(f"{i+1:<4}{k['id']:<6}{k['merk']:<15}{k['warna']:<10}{harga_format:<15}{k['status']:<10}")
    print("-" * 65)

def create(data_list):
    print("\n--- 1. Tambah Data Kendaraan ---")
    while True:
        id_baru = input("Masukkan ID Kendaraan : ").upper()
        if not id_baru:
            print("ID tidak boleh kosong.")
        elif cari_index_data(data_list, id_baru) != -1: 
            print("ID kendaraan sudah ada.")
        else:
            break
    while True:
        try:
            merk = input("Merk Kendaraan: ")
            warna = input("Warna Kendaraan: ")
            harga_sewa = int(input("Harga Sewa per hari: "))
            if harga_sewa > 0: break
            else: print("Harga sewa harus lebih dari nol.")
        except ValueError:
            print("Harga sewa harus berupa angka yang valid.")
    record_baru = {"id": id_baru, "merk": merk, "warna": warna, "harga_sewa": harga_sewa, "status": "Tersedia"}
    data_list.append(record_baru)
    print("\n Data kendaraan berhasil ditambahkan!")
    return data_list

#sorting dengan Bubble Sort (ascending)
def bubble_sort(data_list, kunci):
    n = len(data_list)
    data_sort = data_list[:] 
    for i in range(n):
        sudah_terurut = True
        for j in range(0, n - i - 1):
            if data_sort[j][kunci] > data_sort[j+1][kunci]:
                data_sort[j], data_sort[j+1] = data_sort[j+1], data_sort[j]
                sudah_terurut = False
        if sudah_terurut:
            break
    return data_sort

def read(data_list):
    while True:
        print("\n--- 2. LIHAT DATA KENDARAAN ---")
        print("1. Tampilkan Semua Data")
        print("2. Cari Kendaraan")
        print("3. Urutkan Tampilan")
        print("4. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1-4): ")
        if pilihan == '1':
            tampilkan_data(data_list)
        elif pilihan == '2':
            kata_kunci = input("Masukkan Merk atau ID kendaraan yang dicari: ").upper()
            hasil_pencarian = [k for k in data_list if kata_kunci in k['id'].upper() or kata_kunci in k['merk'].upper()]
            if hasil_pencarian: tampilkan_data(hasil_pencarian)
            else: print(f"\nTidak ditemukan kendaraan dengan kata kunci '{kata_kunci}'.")
        elif pilihan == '3':
            print("Urutkan berdasarkan: (1) ID, (2) Merk, (3) Harga Sewa")
            pilihan_urut = input("Pilih (1/2/3): ")
            kunci = {'1': 'id', '2': 'merk', '3': 'harga_sewa'}.get(pilihan_urut)
            if kunci:
                data_terurut = bubble_sort(data_list, kunci)
                print(f"\nData berhasil diurutkan berdasarkan {kunci.replace('_', ' ').upper()}.")
                tampilkan_data(data_terurut)
            else: print("Pilihan tidak valid.")
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid.")
        jeda()

def update(data_list):
    tampilkan_data(data_list)
    print("\n--- 3. Edit Data Kendaraan ---")
    id_edit = input("Masukkan ID Kendaraan yang akan diedit: ").upper()
    lokasi = cari_index_data(data_list, id_edit)
    if lokasi != -1:
        kendaraan = data_list[lokasi]
        if kendaraan['status'] == "Tersedia":
            print(f"\nData saat ini: Merk={kendaraan['merk']}, Harga={kendaraan['harga_sewa']:,}")
            merk_baru = input(f"Masukkan Merk Baru ({kendaraan['merk']}): ") or kendaraan['merk']
            warna_baru = input(f"Masukkan Warna Baru ({kendaraan['warna']}): ") or kendaraan['warna']
            while True:
                harga_str = input(f"Masukkan Harga Sewa Baru ({kendaraan['harga_sewa']}): ")
                if not harga_str:
                    harga_baru = kendaraan['harga_sewa']; break
                try:
                    harga_baru = int(harga_str)
                    if harga_baru > 0: break
                    else: print("Harga sewa harus lebih dari nol.")
                except ValueError: print("Input harus berupa angka.")
            data_list[lokasi].update({'merk': merk_baru, 'warna': warna_baru, 'harga_sewa': harga_baru})
            print("\n Data kendaraan berhasil diupdate!")
        else:
            print(f" Kendaraan ID {id_edit} sedang '{kendaraan['status']}'. Tidak bisa diedit.")
    else:
        print(" ID Kendaraan tidak ditemukan.")
    return data_list

def delete(data_list):
    tampilkan_data(data_list)
    print("\n--- 4. Hapus Data Kendaraan ---")
    id_hapus = input("Masukkan ID Kendaraan yang akan dihapus: ").upper()
    lokasi = cari_index_data(data_list, id_hapus)
    if lokasi != -1:
        kendaraan = data_list[lokasi]
        if kendaraan['status'] == "Tersedia":
            konfirmasi = input(f" Yakin ingin menghapus {kendaraan['merk']} (Y/T)? ").upper()
            if konfirmasi == 'Y':
                data_list.pop(lokasi)
                print("\n Data kendaraan berhasil dihapus!")
            else:
                print("Operasi hapus dibatalkan.")
        else:
            print(f" Kendaraan ID {id_hapus} sedang '{kendaraan['status']}'. Tidak bisa dihapus.")
    else:
        print(" ID Kendaraan tidak ditemukan.")
    return data_list

def proses_transaksi(data_list):
    while True:
        print("\n--- 5. PROSES TRANSAKSI (SEWA/KEMBALI) ---")
        print("1. Penyewaan Kendaraan")
        print("2. Pengembalian Kendaraan")
        print("3. Kembali ke Menu Utama")
        pilihan_transaksi = input("Pilih (1-3): ")
        if pilihan_transaksi == '1':
            id_sewa = input("Masukkan ID Kendaraan yang akan disewa: ").upper()
            lokasi = cari_index_data(data_list, id_sewa)
            if lokasi != -1 and data_list[lokasi]['status'] == "Tersedia":
                nama_penyewa = input("Nama Penyewa: ")
                lama_sewa = 0
                while lama_sewa <= 0:
                    try:
                        lama_sewa = int(input("Lama Sewa (hari): "))
                        if lama_sewa <= 0: print(" Lama sewa minimal 1 hari.")
                    except ValueError: print(" Input harus berupa angka.")
                data_list[lokasi]['status'] = "Disewa"
                total_biaya = data_list[lokasi]['harga_sewa'] * lama_sewa
                print("\n Penyewaan berhasil!")
                print(f"Total biaya: Rp {total_biaya:,}")
            elif lokasi != -1:
                print(f"\n Kendaraan ID {id_sewa} statusnya '{data_list[lokasi]['status']}'. Tidak bisa disewa.")
            else:
                print(f"\n ID Kendaraan {id_sewa} tidak ditemukan.")
            jeda()
        elif pilihan_transaksi == '2':
            id_kembali = input("Masukkan ID Kendaraan yang dikembalikan: ").upper()
            lokasi = cari_index_data(data_list, id_kembali)
            if lokasi != -1 and data_list[lokasi]['status'] == "Disewa":
                data_list[lokasi]['status'] = "Tersedia"
                print("\n Pengembalian berhasil!")
                print(f"Kendaraan ID {id_kembali} kini berstatus 'Tersedia'.")
            elif lokasi != -1:
                print(f"\n Kendaraan ID {id_kembali} statusnya '{data_list[lokasi]['status']}'. Tidak perlu dikembalikan.")
            else:
                print(f"\n ID Kendaraan {id_kembali} tidak ditemukan.")
            jeda()
        elif pilihan_transaksi == '3':
            break
        else:
            print(" Pilihan tidak valid.")
            jeda()
    return data_list

def laporan_status(data_list):
    print("\n--- 6. LAPORAN STATUS KENDARAAN ---")
    tampilkan_data(data_list) 

    jumlah_tersedia = sum(1 for k in data_list if k['status'] == "Tersedia")
    jumlah_disewa = sum(1 for k in data_list if k['status'] == "Disewa")

    print("\n--- REKAP KENDARAAN ---")
    print(f"Total Semua Kendaraan: {len(data_list)}")
    print(f"Total Kendaraan Tersedia: {jumlah_tersedia}")
    print(f"Total Kendaraan Disewa: {jumlah_disewa}")

def menuUtama():
    print("\n==============================================")
    print(" RodaKampus : Sistem Penyewaan Motor 🏍️")
    print("==============================================")
    print("1. Tambah Data Kendaraan")
    print("2. Lihat Data Kendaraan")
    print("3. Edit Data Kendaraan")
    print("4. Hapus Data Kendaraan")
    print("5. Proses Transaksi (Sewa/Kembali)")
    print("6. Laporan Status Kendaraan")
    print("7. Keluar Program")
    print("==============================================")

    while True:
        try:
            pilihan = int(input("Masukkan pilihan [1 - 7]: "))
            if 1 <= pilihan <= 7:
                return pilihan
            else:
                print("Pilihan hanya antara 1 sampai 7. Silakan coba lagi.")
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

pilihan = 0
data = data_kendaraan 

while (pilihan != 7):
    pilihan = menuUtama()
    if (pilihan == 1):
        data = create(data)
    elif (pilihan == 2):
        read(data)
    elif (pilihan == 3):
        data = update(data)
    elif (pilihan == 4):
        data = delete(data)
    elif (pilihan == 5):
        data = proses_transaksi(data)
    elif (pilihan == 6):
        laporan_status(data)
    if pilihan in [1, 3, 4, 6]:
        jeda()

print("\nTerima kasih, Telah Mengunjungi Sistem Penyewaan Motor Kami. Sampai Jumpa!")
sys.exit()