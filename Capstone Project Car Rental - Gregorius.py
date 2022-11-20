#------- CAPSTONE PROJECT MODULE 1 -------
#----- GREGORIUS WISANGTITIS SETYAJI -----
#-------------- JCDSOL 08 ----------------

#                                                   DICTIONARY UTAMA -----------------------------------------------
dict_mobil= {
    '1001':{
        'ID': '1001',
        'Nama Mobil': 'AVANZA',
        'Tahun Seri': '2020',
        'Warna Mobil': 'SILVER',
        'Tipe Mobil': 'MPV',
        'Status': 'TERSEDIA',
        'Nama Peminjam': '-'
    },
    '1002':{
        'ID':'1002',
        'Nama Mobil':'XENIA',
        'Tahun Seri':'2020',
        'Warna Mobil':'HITAM',
        'Tipe Mobil': 'MPV',
        'Status': 'TERSEDIA',
        'Nama Peminjam':'-'
    },
    '1003':{
        'ID':'1003',
        'Nama Mobil':'AVANZA',
        'Tahun Seri':'2019',
        'Warna Mobil':'HITAM',
        'Tipe Mobil': 'MPV',
        'Status': 'DISEWA',
        'Nama Peminjam':'JARWO'
    },
    '1004':{
        'ID':'1004',
        'Nama Mobil':'C R V',
        'Tahun Seri':'2018',
        'Warna Mobil':'Putih',
        'Tipe Mobil':'SUV',
        'Status': 'PERBAIKAN',
        'Nama Peminjam':'-'
    },
    '1005':{
        'ID':'1005',
        'Nama Mobil':'JIMNY',
        'Tahun Seri':'2021',
        'Warna Mobil':'HITAM',
        'Tipe Mobil': 'SUV',
        'Status': 'DISEWA',
        'Nama Peminjam':'TUMINI'
    }
}

def nodata():                                       # CALLBACK KETIKA LIST KOSONG ----------------------------
    print ('''\n
*********************************************
!!!!!!!!!!!!!! TIDAK ADA DATA !!!!!!!!!!!!!!!
*********************************************
    \n''')


def tidak_tersedia():                               # CALLBACK KETIKA PILIHAN INPUT SALAH/TIDAK TERSEDIA -----
    print ('''
********************************************* 
!!!!!!!!!! PILIHAN TIDAK TERSEDIA !!!!!!!!!!!
*********************************************
    ''')
    print ('''
------- Masukkan Kembali Pilihan Anda -------
    \n''')


def data_tersimpan():                                    # CALLBACK KETIKA DATA BERHASIL TERSIMPAN ----------------
    print ('''
*********************************************
--------- DATA BERHASIL TERSIMPAN -----------
*********************************************''')


def data_terhapus():                                    # CALLBACK KETIKA DATA BERHASIL TERHAPUS ----------------
    print ('''
*********************************************
!!!!!!!!!! DATA BERHASIL DIHAPUS !!!!!!!!!!!!
*********************************************''')


def read_data():                                    # MENU (1) READ DATA -------------------------------------
    pilihan_menu_read = input('''\n\n
*************** DAFTAR MOBIL ****************
__________________
MENU DAFTAR MOBIL:

    1. Lihat Seluruh Daftar Mobil
    2. Cari ID Daftar Mobil
    3. Daftar Mobil Siap Disewa

    0. Kembali Ke Menu Utama

_____________________________________________
Pilih Menu : ''')

    while True:
        if pilihan_menu_read == '1' :
            semua_daftar_mobil()
            break
        elif pilihan_menu_read == '2' :
            cari_daftar()
            break
        elif pilihan_menu_read == '3' :
            cari_tersedia()
            break
        elif pilihan_menu_read == '0' :
            main_menu()
            break
        else :
            tidak_tersedia()
            break


def semua_daftar_mobil():                                   # SUBMENU (1)-(1) LIST DATA DAFTAR MOBIL ------------
    if len(dict_mobil) == 0 :
        nodata()   
    else :
        print ('''
********************************************** DAFTAR SEMUA MOBIL **********************************************\n''')
        print ('''
| ID \t| Nama Mobil \t| Tahun \t| Warna Mobil \t| Tipe Mobil \t| Status \t\t| Nama Peminjam \n''')
        for x in dict_mobil.keys() :
            print (f"| {dict_mobil[x]['ID']} \t| {dict_mobil[x]['Nama Mobil']} \t| {dict_mobil[x]['Tahun Seri']} \t\t| {dict_mobil[x]['Warna Mobil']} \t| {dict_mobil[x]['Tipe Mobil']} \t\t| {dict_mobil[x]['Status']} \t\t| {dict_mobil[x]['Nama Peminjam']}")


def cari_daftar():                                          # SUBMENU (1)-(2) CARI DATA DALAM DAFTAR MOBIL ------
    if dict_mobil == {} :
        nodata()
    else :
        pencarian = input("\n\nMasukkan ID Yang Dicari: ")
        while len(pencarian) != 4 :
            print ('''\n\n ! Masukkan 4 Angka (0-9) ! \n\n''')
            pencarian = input("\n\nMasukkan ID Yang Dicari: ")
        print ('''
************************************************** DAFTAR MOBIL ************************************************\n''')
        print ('''
| ID \t| Nama Mobil \t| Tahun \t| Warna Mobil \t| Tipe Mobil \t| Status \t\t| Nama Peminjam \n''')
        for x in dict_mobil.keys() :
            if pencarian == dict_mobil[x]['ID'] :
                print (f"| {dict_mobil[x]['ID']} \t| {dict_mobil[x]['Nama Mobil']} \t| {dict_mobil[x]['Tahun Seri']} \t\t| {dict_mobil[x]['Warna Mobil']} \t| {dict_mobil[x]['Tipe Mobil']} \t\t| {dict_mobil[x]['Status']} \t\t| {dict_mobil[x]['Nama Peminjam']}")
                break
        if pencarian != dict_mobil[x]['ID']:
            print (f'''\n
        !!! ID : "{pencarian}" Tidak Ditemukan !!!
            \n\n''')

def cari_tersedia():                                        # SUBMENU (1)-(3) CARI DATA MOBIL SIAP DISEWA ----
    if len(dict_mobil) == 0:
        nodata()
    else:
        print ('''
******************************************** DAFTAR MOBIL SIAP DISEWA ******************************************\n''')
        print ('''
| ID \t| Nama Mobil \t| Tahun \t| Warna Mobil \t| Tipe Mobil \t| Status \t\t| Nama Peminjam \n''')
        for x in dict_mobil.keys():
            if dict_mobil[x]['Status'] == 'TERSEDIA' :
                print (f"| {dict_mobil[x]['ID']} \t| {dict_mobil[x]['Nama Mobil']} \t| {dict_mobil[x]['Tahun Seri']} \t\t| {dict_mobil[x]['Warna Mobil']} \t| {dict_mobil[x]['Tipe Mobil']} \t\t| {dict_mobil[x]['Status']} \t\t| {dict_mobil[x]['Nama Peminjam']}")


def create_data():                                  # MENU (2) CREATE DATA -----------------------------------
    pilihan_menu_create = input('''\n\n
************ TAMBAH DATA MOBIL **************
_______________________
MENU TAMBAH DATA MOBIL:

    1. Tambah Data (Input ID Baru)

    0. Kembali Ke Menu Utama

_____________________________________________
Pilih Menu : ''')
    if pilihan_menu_create == '1' :
        tambah_baru()
    elif pilihan_menu_create == '0' :
        main_menu()
    else:
        tidak_tersedia()


def tambah_baru():                                          # SUBMENU (2)-(1) TAMBAH DATA -----------------------
    print ('''
___________________
TAMBAH DATA ID BARU: \n\n''')
    id_baru = input('''Masukkan 4 Angka ID Mobil Baru: ''')
    while len(id_baru) != 4 :
        print ('''\n\n ! Masukkan 4 Angka (0-9) ! \n\n''')
        id_baru = input('''Masukkan 4 Angka ID Mobil Baru: ''')
    for x in dict_mobil.keys() :
        if id_baru == dict_mobil[x]['ID'] :
            print ('''
*********************************************
           !!! Data Sudah Ada !!!''')
            StopIteration
            tambah_baru()
    if id_baru != dict_mobil[x]['ID'] :
        nama_baru = input('''Masukkan Nama Mobil Baru: ''')
        tahun_baru = input('''Masukkan Tahun Seri Mobil Baru: ''')
        warna_baru = input('''Masukkan Warna Mobil Baru: ''')
        tipe_baru = input('''Masukkan Tipe Mobil Baru: ''')
        status_baru = "TERSEDIA"
        peminjam_baru = "-"
        check = input(f'''Input:
ID: {id_baru}
Nama Mobil: {nama_baru}
Tahun Mobil: {tahun_baru}
Warna Mobil: {warna_baru}
Tipe Mobil: {tipe_baru}
\nTambahkan Data? (Y/N): ''')
        while check.lower() != 'y' :
            break
        else:
            dict_mobil[id_baru]={'ID':id_baru, 'Nama Mobil':nama_baru.upper(), 'Tahun Seri':tahun_baru, 'Warna Mobil':warna_baru.upper(), 'Tipe Mobil':tipe_baru.upper(), 'Status':status_baru.upper(), 'Nama Peminjam':peminjam_baru.upper()}
            data_tersimpan()
        semua_daftar_mobil()
        create_data()

        

def update_data():                                  # MENU (3) UPDATE DATA -----------------------------------
    pilihan_menu_update = input('''\n\n
************ UPDATE DATA MOBIL **************
_________________
MENU UPDATE DATA:

    1. Ubah Data (Input ID Mobil)

    0. Kembali Ke Menu Utama

_____________________________________________
Pilih Menu : ''')
    if pilihan_menu_update == '1' :
        update_by_id()
    elif pilihan_menu_update == '0' :
        main_menu()
    else :
        tidak_tersedia()


def update_by_id():                                         # SUBMENU (3)-(1) UPDATE BY ID ----------------------
    semua_daftar_mobil()
    cari_id = input('''\n\nMasukkan 4 Angka ID Mobil (0-9): ''')
    while len(cari_id) != 4 :
        print ('''\n\n ! Masukkan 4 Angka (0-9) ! \n\n''')
        cari_id = input('''\n\nMasukkan 4 Angka ID Mobil (0-9): ''')
    for x in dict_mobil.keys() :
        if cari_id == dict_mobil[x]["ID"] :
            pilihan_update_id = input(f'''
    _________________
    MENU UPDATE DATA:

        1. Ubah Nama Mobil
        2. Ubah Tahun Seri Mobil
        3. Ubah Warna Mobil
        4. Ubah Tipe Mobil
        5. Ubah Status Sewa Mobil
        6. Ubah Nama Peminjam
        
        9. Kembali Ke Menu Sebelumnya
        0. Kembali Ke Menu Utama

    Data ID Ditemukan: "{cari_id}"
    _____________________________________________
    Pilih Menu : ''')
            if pilihan_update_id == '1' :
                ubah_nama = input('''Nama Mobil Diganti Menjadi: ''')
                check_nama = input(f'''Ubah Nama Mobil Menjadi "{ubah_nama}" (Y/N): ''')
                while check_nama.lower() != 'y' :
                    break
                else:
                    dict_mobil[x]['Nama Mobil'] = ubah_nama.upper()
                    data_tersimpan()
                    semua_daftar_mobil()
            elif pilihan_update_id == '2' :
                ubah_tahun = input('''Tahun Seri Mobil Diganti Menjadi: ''')
                check_tahun = input(f'''Ubah Tahun Seri Mobil Menjadi "{ubah_tahun}" (Y/N): ''')
                while check_tahun.lower() != 'y' :
                    break
                else:
                    dict_mobil[x]['Tahun Seri'] = ubah_tahun
                    data_tersimpan()
                    semua_daftar_mobil()
            elif pilihan_update_id == '3' :
                ubah_warna = input('''Warna Mobil Diganti Menjadi: ''')
                check_warna = input(f'''Ubah Warna Mobil Menjadi "{ubah_warna}" (Y/N): ''')
                while check_warna.lower() != 'y' :
                    break
                else:
                    dict_mobil[x]['Warna Mobil'] = ubah_warna.upper()
                    data_tersimpan()
                    semua_daftar_mobil()
            elif pilihan_update_id == '4' :
                ubah_tipe = input('''Tipe Mobil Diganti Menjadi: ''')
                check_tipe = input(f'''Ubah Tipe Mobil Menjadi "{ubah_tipe}" (Y/N): ''')
                while check_tipe.lower() != 'y' :
                    break
                else:
                    dict_mobil[x]['Tipe Mobil'] = ubah_tipe.upper()
                    data_tersimpan()
                    semua_daftar_mobil()
            elif pilihan_update_id == '5' :
                ubah_status = input('''Status Sewa Diganti Menjadi: ''')
                check_status = input(f'''Ubah Status Sewa Menjadi "{ubah_status}" (Y/N): ''')
                while check_status.lower() != 'y' :
                    break
                else:
                    dict_mobil[x]['Status'] = ubah_status.upper()
                    data_tersimpan()
                    semua_daftar_mobil()
            elif pilihan_update_id == '6' :
                ubah_peminjam = input('''Nama Penyewa Diganti Menjadi: ''')
                check_pinjam = input(f'''Ubah Nama Penyewa Menjadi "{ubah_peminjam}" (Y/N): ''')
                while check_pinjam.lower() != 'y' :
                    break
                else:
                    dict_mobil[x]['Nama Peminjam'] = ubah_peminjam.upper()
                    data_tersimpan()
                    semua_daftar_mobil()
            elif pilihan_update_id == '9' :
                update_data()
            elif pilihan_update_id == '0' :
                main_menu()
            else:
                tidak_tersedia()
            update_data()
        if cari_id != dict_mobil[x]["ID"] :
            print (f'''\n
        !!! ID : "{cari_id}" Tidak Ditemukan !!!
            \n\n''')
            update_data()
        


def delete_data():                                  # MENU (4) DELETE DATA -----------------------------------
    semua_daftar_mobil()

    pilihan_menu_delete = input('''
************* HAPUS DATA MOBIL **************
_________________
MENU HAPUS DATA:

    1. Hapus Data (Input ID Mobil)

    0. Kembali Ke Menu Utama

_____________________________________________
Pilih Menu : ''')
    if pilihan_menu_delete == '1' :
        hapus_data()
    elif pilihan_menu_delete == '0' :
        main_menu()
    else:
        tidak_tersedia()


def hapus_data():                                           # SUBMENU (4)-(1) HAPUS DATA -------------------
    semua_daftar_mobil()
    cari_id = input('''\n\nMasukkan 4 Angka ID Mobil (0-9): ''')
    if len(cari_id) != 4 :
        print ('''\n\n ! Masukkan 4 Angka (0-9) ! \n\n''')
        cari_id = input('''\n\nMasukkan 4 Angka ID Mobil (0-9): ''')
    print ('''
| ID \t| Nama Mobil \t| Tahun \t| Warna Mobil \t| Tipe Mobil \t| Status \t\t| Nama Peminjam \n''')
    for x in dict_mobil.keys() :
        if cari_id == dict_mobil[x]['ID'] :
            print (f"| {dict_mobil[x]['ID']} \t| {dict_mobil[x]['Nama Mobil']} \t| {dict_mobil[x]['Tahun Seri']} \t\t| {dict_mobil[x]['Warna Mobil']} \t| {dict_mobil[x]['Tipe Mobil']} \t\t| {dict_mobil[x]['Status']} \t\t| {dict_mobil[x]['Nama Peminjam']}")
            pilihan_hapus_id = input(f'''\n\n!!! Anda Yakin Hapus Entry Dengan ID "{cari_id}:? (Y/N): ''')
            while pilihan_hapus_id.lower() != 'y' :
                break
            else:
                del dict_mobil[x]
                data_terhapus()
                delete_data()
        StopIteration
        break
    if cari_id != dict_mobil[x]['ID'] :
        print (f'''\n
!!! ID : "{cari_id}" Tidak Ditemukan !!!
    \n\n''')
        
                

def main_menu():
    pilihan_menu_utama = input('''\n\n
***********************************************
------------ RENTAL MOBIL SEJAHTERA ----------- 
***********************************************

___________
MENU UTAMA:

    1. Daftar Mobil
    2. Tambah Data Ke Daftar Mobil
    3. Ubah Data Dalam Daftar Mobil
    4. Hapus Data Dalam Daftar Mobil
    5. Keluar

_____________________________________________
Pilih Menu (1 - 5): ''')

    while True:
        if pilihan_menu_utama == '1':
            read_data()
        elif pilihan_menu_utama == '2':
            create_data()
        elif pilihan_menu_utama == '3':
            update_data()
        elif pilihan_menu_utama == '4':
            delete_data()
        elif pilihan_menu_utama == '5':
            print ('''\n\n
===============================================
------------ SAMPAI JUMPA KEMBALI -------------
===============================================
            \n\n''')
            StopIteration
            quit()
        else:
            tidak_tersedia()
            main_menu()

main_menu()
