from model.daftar_nilai import *
from view.view_nilai import *

while True:
    i = input("\nA)dd, E)dit, S)earch, D)elete L)ist, Q)uit: ")

    if (i.lower() == 'a'):
        tambah_data()

    elif (i.lower() == 'e'):
        ubah_data()

    elif (i.lower() == 's'):
        cetak_hasil_pencarian()

    elif (i.lower() == 'd'):
        hapus_data()

    elif (i.lower() == 'l'):
        cetak_daftar_nilai()

    elif (i.lower() == 'q'):
        break

    else:
        print("Silahkan pilih menu yang tersedia!")