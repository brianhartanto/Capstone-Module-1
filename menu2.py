import sys
sys.path.append('../db/data_karyawan')
import db.data_karyawan as db
import os
def print_menu():
    while True:
        print('''=============Report Data Karyawan=============
        1.Tambah Data Siswa
        2.Kembali ke Menu Utama ''')

        UserInput =int(input(f'Silahkan Pilih Sub Menu Data [1-2]:'))
        if UserInput == 1 :
            nama_karyawan = (input('masukan nama karyawan :'))
            flag = True
            for key in range (len(db.data_karyawan)) :
                NAMA = db.data_karyawan[key]['namakaryawan']
                if nama_karyawan == NAMA:
                    os.system('cls||clear')
                    print('nama anda sudah ada di dalam database')
                    flag = False
                    break

            if flag:
                os.system('cls||clear')

                umur_karyawan = (input('masukan umur karyawan :'))
                jenis_kelamin_karyawan = (input('masukan jenis kelamin karyawan:'))
                gaji_karyawan = (input('masukan gaji karyawan:'))
                jabatan_karyawan = (input('masukan jabatan:'))

                new_karyawan = { #DICT BARU menampung data baru untuk dimasukan ke dalam database
                                'namakaryawan' :  nama_karyawan,
                                'umur'         :  umur_karyawan  ,
                                'jabatan'      :  jabatan_karyawan ,
                                'jeniskelamin' :   jenis_kelamin_karyawan ,
                                'gaji'         :    gaji_karyawan
                                }
                db.data_karyawan.append(new_karyawan)
        if UserInput == 2 :

            break
