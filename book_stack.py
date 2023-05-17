class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis


class BukuStack:
    def __init__(self):
        self.stack = []

    # Menambahkan Buku
    def tambah_buku(self, buku):
        self.stack.append(buku)
        print(
            f"Buku '{buku.judul}' oleh {buku.penulis} telah ditambahkan ke dalam tumpukan.")

    # Menghapus Buku
    def hapus_buku(self):
        if len(self.stack) > 0:
            buku = self.stack.pop()
            print(
                f"Buku '{buku.judul}' oleh {buku.penulis} telah dihapus dari tumpukan.")
        else:
            print("Tumpukan buku kosong.")

    # Menampilkan Buku Teratas
    def teratas_buku(self):
        if len(self.stack) > 0:
            buku = self.stack[-1]
            print(f"Buku teratas: '{buku.judul}' oleh {buku.penulis}.")
        else:
            print("Tumpukan buku kosong.")

    # Menampilkan Seluruh Buku
    def tampilkan_bukus(self):
        if len(self.stack) > 0:
            print("Buku yang tersimpan:")
            for buku in self.stack:
                print(f"'{buku.judul}' oleh {buku.penulis}")
        else:
            print("Tumpukan buku kosong.")


buku_stack = BukuStack()

while True:
    print("\nMenu:")
    print("1. Tambahkan Buku")
    print("2. Hapus Buku Terakhir")
    print("3. Tampilkan Buku Teratas")
    print("4. Tampilkan Semua Buku")
    print("5. Keluar")

    pilih = input("Pilih tindakan (1/2/3/4/5): ")

    if pilih == "1":
        buku_judul = input("Masukkan judul buku: ")
        buku_penulis = input("Masukkan nama pengarang: ")
        buku = Buku(buku_judul, buku_penulis)
        buku_stack.tambah_buku(buku)
    elif pilih == "2":
        buku_stack.hapus_buku()
    elif pilih == "3":
        buku_stack.teratas_buku()
    elif pilih == "4":
        buku_stack.tampilkan_bukus()
    elif pilih == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
