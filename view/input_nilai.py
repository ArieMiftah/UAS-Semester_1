from model.daftar_nilai import tambah_data, hapus_data, ubah_data
from view.view_nilai import cari

def masukan_data():
    print("=================")
    print("| Masukkan Data |")
    print("=================")

    nama = input("Masukan Nama        = ")
    nim = int(input("Masukan NIM         = "))
    tugas = int(input("Masukan Nilai Tugas = "))
    uts = int(input("Masukan Nilai UTS   = "))
    uas = int(input("Masukan Nilai UAS   = "))
    nilai_akhir= float(30/100*tugas)+(35/100*uts)+(35/100*uas)
    tambah_data(nama, nim, tugas, uts, uas, nilai_akhir)

def cari_hapus():
    hapus_data(input(" Masukkan data yang ingin dihapus = "))

def cari_ubah():
    ubah_data(input(" Masukkan nama yang diubah = "))

    print("======================")
    print("| Masukkan Data Baru |")
    print("======================")

    nama = input("Masukan Nama        = ")
    nim = int(input("Masukan NIM         = "))
    tugas = int(input("Masukan Nilai Tugas = "))
    uts = int(input("Masukan Nilai UTS   = "))
    uas = int(input("Masukan Nilai UAS   = "))
    nilai_akhir = float(30 / 100 * tugas) + (35 / 100 * uts) + (35 / 100 * uas)
    tambah_data(nama, nim, tugas, uts, uas, nilai_akhir)