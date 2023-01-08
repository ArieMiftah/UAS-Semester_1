data = {}

def tambah_data(nama, nim, tugas, uts, uas, nilai_akhir):
    data[nama] = nama, nim, tugas, uts, uas, nilai_akhir

def ubah_data(nama):
    if nama in data.keys():
        del data[nama]
    else:
        print(f"Data dengan nama {nama} Tidak ditemukan!")

def hapus_data(nama):
    if nama in data.keys():
        del data[nama]
        print(f"Data dengan nama {nama} Telah dihapus!")
        return  True
    else:
        print(f"Data dengan nama {nama} Tidak ditemukan!")
        print()
        return False

def cari_data():
    from view.view_nilai import cari
    cari(input("Masukkan nama yang ingin dicari = "))