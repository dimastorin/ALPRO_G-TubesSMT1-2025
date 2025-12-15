data_penilaian = []
no_gtg = 1

def n_ke_a(n):
    n = n.upper()
    if n == "I":
        return 4
    elif n == "II":
        return 3
    elif n == "III":
        return 2
    elif n == "IV":
        return 1
    else:
        return 0

def create():
    global no_gtg
    print("Input data baru")
    suara1 = input("Suara I  (I/II/III/IV): ")
    suara2 = input("Suara II (I/II/III/IV): ")
    suara3 = input("Suara III(I/II/III/IV): ")
    suara4 = input("Suara IV (I/II/III/IV): ")
    cad1 = input("Cadangan 1: ")
    cad2 = input("Cadangan 2: ")
    dasar = input("Dasar Suara: ")
    gaya = input("Gaya Irama: ")
    juara = input("Juara: ")
    total = n_ke_a(suara1) + n_ke_a(suara2) + n_ke_a(suara3) + n_ke_a(suara4)

    data_penilaian.append({
        "gtg": no_gtg,
        "suara": [suara1, suara2, suara3, suara4],
        "total": total,
        "cad1": cad1,
        "cad2": cad2,
        "dasar": dasar,
        "gaya": gaya,
        "juara": juara
    })

    print("Data tersimpan!")
    no_gtg += 1

def read():
    if not data_penilaian:
        print("Belum ada data.")
        return

    print("=== DATA ===")
    for d in data_penilaian:
        print(f"""
GTG : {d['gtg']}
Suara : {d['suara']}
Total Nilai : {d['total']}
Cad 1 : {d['cad1']}
Cad 2 : {d['cad2']}
Dasar : {d['dasar']}
Gaya  : {d['gaya']}
Juara : {d['juara']}
---------------------------""")

def update():
    if not data_penilaian:
        print("Belum ada data")
        return

    gtg = int(input("GTG yang diupdate: "))

    for d in data_penilaian:
        if d["gtg"] == gtg:
            print("Kosongkan jika tidak diganti")
            for i in range(4):
                new = input(f"Suara {i+1}: ")
                if new:
                    d["suara"][i] = new
            d["cad1"] = input("Cad 1: ") or d["cad1"]
            d["cad2"] = input("Cad 2: ") or d["cad2"]
            d["dasar"] = input("Dasar: ") or d["dasar"]
            d["gaya"]  = input("Gaya : ") or d["gaya"]
            d["juara"] = input("Juara: ") or d["juara"]
            d["total"] = sum(n_ke_a(x) for x in d["suara"])
            print("Data diperbarui!")
            return
    print("GTG tidak ditemukan.")

def delete():
    if not data_penilaian:
        print("Belum ada data")
        return

    gtg = int(input("GTG yang dihapus: "))
    for d in data_penilaian:
        if d["gtg"] == gtg:
            data_penilaian.remove(d)
            print("Data dihapus!")
            return
    print("GTG tidak ditemukan.")

def menu():
    print("======================================")
    print("      SISTEM PENILAIAN LOMBA BURUNG   ")
    print("======================================")
    while True:
        print("""
1. Tambah
2. Lihat
3. Update
4. Hapus
5. Keluar
""")
        p = input("Pilih: ")

        if p == "1":
            create()
        elif p == "2":
            read()
        elif p == "3":
            update()
        elif p == "4":
            delete()
        elif p == "5":
            print("Terima kasih telah menggunakan Sistem Penilaian Lomba burung.")
            break
        else:
            print("Salah input!")
menu()