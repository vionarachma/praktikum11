# praktikum-11
## Bahasa Pemrograman { Tugas Pertemuan ke 11 }
###  Program sederhana dengan mengaplikasikan penggunaan fungsi yang akan menampilkan daftar nilai mahasiswa

### FLOWCHART :
  - ![img](https://github.com/raissaputra/praktikum-11/blob/main/assets/flowchart.png)
  
### OUTPUT PROGRAM `fungsiNilai.py`:
  - Tampilan Awal Program
  - ![img](https://github.com/raissaputra/praktikum-11/blob/main/assets/awalMenu.png)
  - Pilih 1 ==> Tambah data :
  - ![img](https://github.com/raissaputra/praktikum-11/blob/main/assets/tambahData.png)
  - Pilih 2 ==> Tampilkan data setelah di tambah data :
  - ![img](https://github.com/raissaputra/praktikum-11/blob/main/assets/tampilkanData.png)
  - Pilih 2 ==> Tampilkan data yang sudah banyak ditambahkan sebelumnya :
  - ![img](https://github.com/raissaputra/praktikum-11/blob/main/assets/tampilBykDt.png)
  - Pilih 3 ==> Ubah data nama :
  - ![img](https://github.com/raissaputra/praktikum-11/blob/main/assets/ubahNama.png)
  - Pilih 4 ==> Hapus Data nama :
  - ![img](https://github.com/raissaputra/praktikum-11/blob/main/assets/hapusNama.png)
  - Pilih 1 ==> Untuk melihat semua perubahan data yang sudah di ubah nama dan ada yang di hapus nama nya :
  - ![img](https://github.com/raissaputra/praktikum-11/blob/main/assets/tampilAfterUbahHapus.png)
  - Pilih 5 ==> Untuk keluar program

### PENJELASAN :
  - Program Nilai sederhana dengan CRUD (create, read, update, delete) memakai fungsi
  - Selama looping bernilai True maka program akan berjalan terus, berikut kode nya:
  - ```
    if __name__ == "__main__":
        while(True):
            menu_nilai()
    ```
  - Inputan dari User akan di append() ke variabel global yang sudah di buat
  - Untuk ubah data dengan parameter nama sebagai indeks nya, berikut kode nya :
  - ```
    i = int(input('Inputkan ID Nama : '))
    if (i > len(nama[i])):
        print('ID Salah')
    else:
        nama_baru = input('Nama Baru : ')
        nama[i] = nama_baru
    ```
  - Untuk hapus data dengan memakai parameter nama sebagai indeks nya, berikut kode nya :
  - ```
    i = int(input('Masukkan ID Mahasiswa: '))
    if (i > len(nama[i])):
        print('ID Salah')
    else:
        nama.remove(nama[i])
    ```
  - Perhitungan nilai akhir ( tugas*(30/100), uts*(35/100), uas*(35/100) )
