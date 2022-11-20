*************************************************************************************************************************
------------------------------------------ WELCOME TO MY FIRST PROJECT :) -----------------------------------------------
*************************************************************************************************************************

-------------------------------------------------------------------------------------------------------------------------
                                    Capstone Project Simple Program Python Based
-------------------------------------------------------------------------------------------------------------------------

** Dictionary default berisi 5 entry.

** Atribut dari dictionary berisi:
	- ID (str)		= Unique ID (Plat Mobil)
	- Nama Mobil (str)	= Nama Mobil
	- Tahun Seri Mobil (str)= Tahun Pembuatan Mobil
	- Warna Mobil (str)	= Warna Mobil
	- Tipe Mobil (str)	= Tipe Mobil (SUV, Sedan, MPV)
	- Status (str)		= Status peminjaman (Tersedia, Disewa, Perbaikan)
	- Nama Peminjam (str)	= Nama Peminjam/Penyewa

** Semua input untuk fitur pencarian menggunakan key ['ID'], berupa 4 angka (0-9).
    Jika tidak 4 angka maka akan dikembalikan ke perintah input.
    Jika input tidak ditemukan, akan dimunculkan notifikasi "ID {xxx} tidak ditemukan".

** Terdapat callback fuction (hanya fungsi print)
	- Ketika pilihan input salah/tidak tersedia
	- Ketika isi dictionary kosong
	- Ketika data berhasil tersimpan
	- Ketika data berhasil terhapus

-------------------------------------------------------------------------------------------------------------------------

Terdapat 5 Menu Utama:
    1. Daftar Mobil
    2. Tambah Data Ke Daftar Mobil
    3. Ubah Data Dalam Daftar Mobil
    4. Hapus Data Dalam Daftar Mobil
    5. Keluar

** Tiap menu sudah memiliki fungsi tersendiri agar mudah dipanggil.

-------------------------------------------------------------------------------------------------------------------------
--- MENU 1 DAFTAR MOBIL

Pada menu ini terdapat 4 sub-menu:
    1. Lihat Seluruh Daftar Mobil	= Print semua data yang ada di dictionary
    2. Cari ID Daftar Mobil		= Fitur cari data berdasarkan ID
    3. Daftar Mobil Siap Disewa		= Print semua data di dictionary yang memiliki key['Status'] = 'Tersedia'
    0. Kembali Ke Menu Utama		= Back to main menu


-------------------------------------------------------------------------------------------------------------------------
--- MENU 2 TAMBAH DATA

Pada menu ini terdapat 2 sub-menu:
    1. Tambah Data (Input ID Baru)	= Tambah data jika input ID belum ada di dalam key['ID']
					  User akan diminta menginput semua key (Nama Mobil, Tahun Seri, Warna, Model),
					  untuk key Status dan Peminjam defaul ('Tersedia', '-').
					  Penambahan input ke dalam dictionary akan dimasukkan secara kapital semua
    0. Kembali Ke Menu Utama		= Back to main menu

-------------------------------------------------------------------------------------------------------------------------
--- MENU 3 UBAH DATA

Pada menu ini terdapat 2 sub-menu:
    1. Ubah Data (Input ID Mobil)	= Input ID mobil, jika ID ditemukan maka akan muncul pilihan key mana yang akan diubah
					  Setiap memasukkan perubahan key, akan ditanya ulang (Y/N)
					  Setiap data yang berhasil terubah akan muncul "Data Berhasil Tersimpan"
    0. Kembali Ke Menu Utama		= Back to main menu

-------------------------------------------------------------------------------------------------------------------------
--- MENU 4 HAPUS DATA

Pada menu ini terdapat 2 sub-menu:
    1. Hapus Data (Input ID Mobil)	= Input ID mobil, jika ID ditemukan akan ditampilkan setiap key milik ID tersebut,
					  Selanjutnya akan ditanya apakah ingin menghapus data (Y/N)
    0. Kembali Ke Menu Utama		= Back to main menu

-------------------------------------------------------------------------------------------------------------------------
--- MENU 5 KELUAR

Exit Program

-------------------------------------------------------------------------------------------------------------------------
