class Transaksi:
    def __init__(self, nama_pelanggan, tipe_transaksi):
        self.nama_pelanggan = nama_pelanggan
        self.tipe_transaksi = tipe_transaksi


class transaksiQueue:
    def __init__(self):
        self.queue = []

    def masukkan_transaksi(self, transaksi):
        self.queue.append(transaksi)
        print(
            f"Transaksi '{transaksi.tipe_transaksi}' oleh {transaksi.nama_pelanggan} telah ditambahkan ke dalam Antrian.")

    def pelayanan(self):
        if len(self.queue) > 0:
            transaksi = self.queue.pop(0)
            print(
                f"Transaksi '{transaksi.tipe_transaksi}' oleh {transaksi.nama_pelanggan} telah dilayani.")
        else:
            print("Antrian transaksi kosong.")

    def transaksi_selanjutnya(self):
        if len(self.queue) > 0:
            transaksi = self.queue[0]
            print(
                f"Transaksi berikutnya: '{transaksi.tipe_transaksi}' oleh {transaksi.nama_pelanggan}.")
        else:
            print("Antrian transaksi kosong.")

    def menampilkan_transaksi(self):
        if len(self.queue) > 0:
            print("Transaksi yang tersimpan:")
            for transaksi in self.queue:
                print(
                    f"'{transaksi.tipe_transaksi}' oleh {transaksi.nama_pelanggan}")
        else:
            print("Antrian transaksi kosong.")


transaksi_queue = transaksiQueue()

while True:
    print("\nMenu:")
    print("1. Tambahkan transaksi")
    print("2. Layani transaksi berikutnya")
    print("3. Tampilkan transaksi berikutnya")
    print("4. Tampilkan semua transaksi")
    print("5. Hapus transaksi yang telah dilayani")
    print("6. Keluar")

    pilih = input("Pilih tindakan (1/2/3/4/5/6): ")

    if pilih == "1":
        nama_pelanggan = input("Masukkan nama pelanggan: ")
        tipe_transaksi = input("Masukkan jenis transaksi: ")
        transaksi = Transaksi(nama_pelanggan, tipe_transaksi)
        transaksi_queue.masukkan_transaksi(transaksi)
    elif pilih == "2":
        transaksi_queue.pelayanan()
    elif pilih == "3":
        transaksi_queue.transaksi_selanjutnya()
    elif pilih == "4":
        transaksi_queue.menampilkan_transaksi()
    elif pilih == "5":
        transaksi_queue.pelayanan()
    elif pilih == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
