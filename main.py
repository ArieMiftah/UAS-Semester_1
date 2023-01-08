import model
import view
import os

while True:
    print("===========================")
    print("|            MENU         |")
    print("===========================")
    print("| 1 |     Tambah Data     |")
    print("| 2 |     Hapus Data      |")
    print("| 3 |     Ubah Data       |")
    print("| 4 |     Cari Data       |")
    print("| 5 |     Tampilkan Data  |")
    print("| 6 |     Keluar Program  |")
    print("===========================")
    pilih= input("Masukkan Pilihan Anda = ")
    print()

    if pilih == '1':
        from view.input_nilai import masukan_data
        masukan_data()

    elif pilih == '2':
        from view.input_nilai import cari_hapus
        cari_hapus()

    elif pilih == '3':
        from view.input_nilai import  cari_ubah
        cari_ubah()

    elif pilih == '4':
        from model.daftar_nilai import cari_data
        cari_data()

    elif pilih == '5':
        from view.view_nilai import tampilkan
        tampilkan()

    elif pilih == '6':
        print(" Terima Kasih")
        break

    else:
        print("Masukkan pilihan yang benar!")