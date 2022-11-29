import sys
sys.path.append('../db/data_karyawan')
import db.data_karyawan as db
import os

def print_menu():
    while True:  #diigunakan untuk looping sampai hasilnya false atau boolean
        print('''=============Report Data Karyawan=============
        1. Report Seluruh Data
        2. Report Data tertentu
        3. Kembali ke menu Utama
        ''')

        user_input = int(input(f'Silahkan Pilih Sub Menu Data [1-3]:'))
        if user_input == 1 :
            os.system('cls||clear')
            print(f"{'namakaryawan':<20}|{'umur':<20}|{'jabatan':<20}|{'jenisKelamin':<20}{'gaji':<20}")

            for key in range (len(db.data_karyawan)) :

                NAMA = db.data_karyawan[key]['namakaryawan'] #digunakan untuk manampung data yang berisi nama karyawan di dalam dict
                UMUR = db.data_karyawan[key]['umur']
                JABATAN= db.data_karyawan[key]['jabatan']
                JENISKELAMIN= db.data_karyawan[key]['jeniskelamin']
                GAJI = db.data_karyawan[key]['gaji']

                print(f"{NAMA:<20}|{UMUR:<20}|{JABATAN:<20}|{JENISKELAMIN:<20}|{GAJI:<20}")

        elif user_input == 2:
            os.system('cls||clear')
            # is_found = False
            nama = (input('Masukan Nama:'))
            flag = False #untuk penanda jika data nama  yang diinginkan ditemukan
            for key in range (len(db.data_karyawan)) :
                if nama == db.data_karyawan[key]['NamaKaryawan']:  #jika nama ditemukan di dalam database makan
                    NAMA = db.data_karyawan[key]['NamaKaryawan']
                    UMUR = db.data_karyawan[key]['Umur']
                    JABATAN= db.data_karyawan[key]['Jabatan']
                    JENISKELAMIN= db.data_karyawan[key]['JenisKelamin']
                    GAJI = db.data_karyawan[key]['Gaji']
                    flag = True # artinya datanya ditemukan
            if flag: #jika data tsb ditemukan

                print(f"{NAMA:<20}|{UMUR:<20}|{JABATAN:<20}|{JENISKELAMIN:<20}|{GAJI:<20}")

                # is_found = True
            else:

                print('Data tidak ditemukan')

        elif user_input == 3:
            break
