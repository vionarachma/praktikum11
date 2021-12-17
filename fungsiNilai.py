nama = []
nim = []
kelas = []
tugas = []
uts = []
uas = []
akhir = []


def menu_nilai():
    print('=========================================')
    print('Input Data Nilai Mahasiswa'.center(40))
    print('=========================================')
    print('| 1. Tambah Data                        |')
    print('| 2. Tampilkan Data                     |')
    print('| 3. Ubah Data                          |')
    print('| 4. Hapus Data                         |')
    print('| 5. Exit                               |')
    print('=========================================')
    pilih = input('Pilih Menu : ')
    if pilih == '1':
        tambah()
    elif pilih == '2':
        tampilkan()
    elif pilih == '3':
        ubah()
    elif pilih == '4':
        hapus()
    elif pilih == '5':
        exit()
    else:
        print('SALAH PILIH ! ')


def judul():
    print('=========================================')
    print('| PROGRAM NILAI MAHASISWA DENGAN FUNGSI |')
    print('=========================================')


def tambah():
    judul()
    print('Tambah Data'.center(40))
    print('=========================================')
    new_nama = input('Nama\t\t: ')
    nama.append(new_nama)

    new_nim = input('NIM\t\t: ')
    nim.append(new_nim)

    new_kelas = input('Kelas\t\t: ')
    kelas.append(new_kelas)

    new_tugas = float(input('Nilai Tugas\t: '))
    n_tugas = new_tugas*(30/100)
    tugas.append(n_tugas)

    new_uts = float(input('Nilai UTS\t: '))
    n_uts = new_uts*(35/100)
    uts.append(n_uts)

    new_uas = float(input('Nilai UAS\t: '))
    n_uas = new_uas*(35/100)
    uas.append(n_uas)

    new_akhir = n_tugas + n_uts + n_uas
    akhir.append(new_akhir)

    print('-----------------------')
    print('Data berhasil di simpan')

    menu_nilai()


def tampilkan():
    judul()
    print('Tampilkan Data'.center(40))
    print('=========================================')

    for i in range(len(nim)):
        print('%d.  Nama        : %s' % (i+1, nama[i]))
        print('    Nim         : %s' % nim[i])
        print('    Kelas       : %s' % kelas[i])
        print('    Tugas       : %.2f' % tugas[i])
        print('    UTS         : %.2f' % uts[i])
        print('    UAS         : %.2f' % uas[i])
        print('    Nilai Akhir : %.2f' % akhir[i])


def hapus():
    judul()
    print('Hapus Data'.center(40))
    print('=========================================')
    i = int(input('Masukkan ID Mahasiswa: '))
    if (i > len(nama[i])):
        print('ID Salah')
    else:
        nama.remove(nama[i])
    print('----------------------')
    print('Nama berhasil di hapus')
    menu_nilai()


def ubah():
    judul()
    print('Ubah Data'.center(40))
    print('=========================================')
    i = int(input('Inputkan ID Nama : '))
    if (i > len(nama[i])):
        print('ID Salah')
    else:
        nama_baru = input('Nama Baru : ')
        nama[i] = nama_baru
    print('---------------------')
    print('Nama berhasil di ubah')
    menu_nilai()


if __name__ == "__main__":
    while(True):
        menu_nilai()
