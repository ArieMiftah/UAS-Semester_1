from model.daftar_nilai import data
from tabulate import tabulate

def tampilkan():
    print(tabulate(data.values(), headers=("Nama", "NIM", "Tugas", "UTS", "UAS", "Nilai Akhir"), tablefmt="double_grid"))

def cari(nama):
    data_cari = {}
    for key, value in data.items():
        if nama in value:
            data_cari[key] = value
            print(tabulate(data_cari.values(), headers=("Nama", "NIM", "Tugas", "UTS", "UAS", "Nilai Akhir"), tablefmt="double_grid"))
        else:
            print(f"Data dengan nama {nama} Tidak ditemukan!")