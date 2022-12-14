import sys
sys.path.append('../db/data_karyawan')
import db.data_karyawan as db
import os
def print_menu():
   while True:
        print('''=============Menghapus Data Karyawan=============
        1.Hapus Data Karyawan
        2.Menghapus seluruh data karyawan
        3.Kembali ke Menu Utama ''')

        UserInput =int(input(f'Silahkan Pilih Sub Menu Data [1-2]: '))
        if UserInput == 1:
            os.system('cls||clear')
            pertanyaan =input('masukan nama karyawan: ')
            flag = False
            for key in range(len(db.data_karyawan)):
                if pertanyaan == db.data_karyawan[key]['namakaryawan']:
                    flag = True
                    break

            if flag :

                del db.data_karyawan[key]
                print('data telah dihapus')
                print(f"{'namakaryawan':<20}|{'umur':<20}|{'jabatan':<20}|{'jeniskelamin':<20}{'gaji':<20}")

                for key in range (len(db.data_karyawan)) :

                    NAMA = db.data_karyawan[key]['namakaryawan']
                    UMUR = db.data_karyawan[key]['umur']
                    JABATAN= db.data_karyawan[key]['jabatan']
                    JENISKELAMIN= db.data_karyawan[key]['jenisKelamin']
                    GAJI = db.data_karyawan[key]['gaji']

                    print(f"{NAMA:<20}|{UMUR:<20}|{JABATAN:<20}|{JENISKELAMIN:<20}|{GAJI:<20}")
            else:
                print('data tidak ditemukan.')
        elif UserInput == 2:
            print('Seluruh data karyawan telah dihapus')
            db.data_karyawan.clear()

        elif UserInput == 3:
            os.system('cls||clear')


            break
