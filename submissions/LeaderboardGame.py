def create(data):
    print("\n=== Tambah Pemain Baru ===")
    try:
        # Meminta input nama pemain dan menghapus spasi di awal/akhir
        nama = input("Masukkan nama pemain: ").strip()

        # Cek apakah nama sudah ada
        for p in data:
            if p[0].lower() == nama.lower():
                print("Nama pemain sudah ada di leaderboard!")
                return data

        # Mengambil input skor pemain dan konversi ke integer
        skor = int(input("Masukkan skor pemain: "))

        # Validasi: skor tidak boleh negatif
        if skor < 0:
            print("Skor tidak boleh negatif.")
            return data

        # Menambahkan pemain baru ke data (list 2D)
        data.append([nama, skor])
        print("Data pemain berhasil ditambahkan.")

    except ValueError:
        # Menangani jika input skor bukan angka
        print("Input tidak valid, skor harus berupa angka.")
    return data


def read(data):
    # Cek apakah data kosong
    if not data:
        print("\nBelum ada data pemain.")
        return

    print("\n=== Lihat Leaderboard ===")
    print("1. Tampilkan semua (urut skor tertinggi)")
    print("2. Cari pemain berdasarkan nama")
    # Meminta pilihan tampilan
    pilihan = input("Pilih (1/2): ").strip()

    if pilihan == "1":
        # Membuat salinan data agar list asli tidak berubah saat diurutkan
        sorted_data = data[:]
        n = len(sorted_data)
        # Proses pengurutan (bubble sort) berdasarkan skor, descending
        for i in range(n):
            for j in range(0, n - i - 1):
                if sorted_data[j][1] < sorted_data[j + 1][1]:
                    sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]

        # Menampilkan leaderboard yang sudah diurutkan
        print("\n=== Leaderboard Game ===")
        print("=" * 40)
        for i, p in enumerate(sorted_data, start=1):
            print(f"{i}. {p[0]:15} | Skor: {p[1]}")
        print("=" * 40)

    elif pilihan == "2":
        # Meminta nama pemain untuk dicari
        cari = input("Masukkan nama pemain: ").strip().lower()
        found = False
        # Mencari pemain pada data
        for p in data:
            if p[0].lower() == cari:
                print(f"\nPemain ditemukan: {p[0]} (Skor: {p[1]})")
                found = True
                break
        # Jika tidak ditemukan
        if not found:
            print("Pemain tidak ditemukan di leaderboard.")

    else:
        # Jika input pilihan tidak valid
        print("Pilihan tidak valid.")
    print()


def update(data):
    # Cek apakah data kosong
    if not data:
        print("\nBelum ada data pemain.")
        return data

    # Meminta nama pemain yang ingin diupdate
    nama = input("\nMasukkan nama pemain yang ingin diupdate: ").strip().lower()

    # Mencari pemain dalam data
    for p in data:
        if p[0].lower() == nama:
            print(f"Data ditemukan: {p[0]} (Skor: {p[1]})")
            try:
                # Meminta skor baru dan konversi ke integer
                skor_baru = int(input("Masukkan skor baru: "))
                # Validasi skor baru
                if skor_baru < 0:
                    print("Skor tidak boleh negatif.")
                    return data

                # Update skor pemain
                p[1] = skor_baru
                print("Skor pemain berhasil diperbarui.")
            except ValueError:
                # Tangani jika input bukan angka
                print("Input tidak valid. Skor harus angka.")
            return data

    # Jika pemain tidak ditemukan
    print("Pemain tidak ditemukan.")
    return data


def delete(data):
    # Cek apakah ada data untuk dihapus
    if not data:
        print("\nBelum ada data untuk dihapus.")
        return data

    # Meminta nama pemain yang ingin dihapus
    nama = input("\nMasukkan nama pemain yang ingin dihapus: ").strip().lower()

    # Mencari pemain berdasarkan indeks
    for i, p in enumerate(data):
        if p[0].lower() == nama:
            # Konfirmasi penghapusan ke user
            konfirmasi = input(f"Yakin hapus {p[0]}? (y/n): ").lower()
            if konfirmasi == "y":
                # Menghapus pemain dari list
                data.pop(i)
                print("Data pemain berhasil dihapus.")
            else:
                # Jika dibatalkan
                print("Penghapusan dibatalkan.")
            return data

    # Jika pemain tidak ditemukan
    print("Pemain tidak ditemukan.")
    return data


def menuUtama():
    # Menampilkan menu utama
    print(" \n=== Leaderboard Game === ")
    print("1. Tambah Pemain")
    print("2. Lihat Leaderboard")
    print("3. Update Skor Pemain")
    print("4. Hapus Pemain")
    print("5. Keluar")

    try:
        # Input pilihan menu dan konversi ke integer
        pilihan = int(input("Masukkan pilihan [1 - 5]: "))
        # Validasi rentang pilihan
        if pilihan < 1 or pilihan > 5:
            print("Pilihan hanya 1 - 5.")
            input("Tekan ENTER untuk lanjut...")
            return 0
        else:
            return pilihan
    except ValueError:
        # Tangani jika input bukan angka
        print("Input harus berupa angka.")
        return 0


##### PROGRAM UTAMA #####
pilihan = 0
data = [
    ["Rizky", 2500],
    ["Sinta", 4200],
    ["Andi", 3100],
    ["Bunga", 1800],
    ["Dewi", 3700]
]

# Loop menu hingga user memilih keluar (5)
while pilihan != 5:
    pilihan = menuUtama()
    if pilihan == 1:
        data = create(data)
    elif pilihan == 2:
        read(data)
        input("Tekan ENTER untuk kembali ke menu...")
    elif pilihan == 3:
        data = update(data)
    elif pilihan == 4:
        data = delete(data)
    else :   
        print("\nTerima kasih telah menggunakan program Leaderboard Game!")
