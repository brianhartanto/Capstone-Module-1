import sys
sys.path.append('../db/data_karyawan')
import db.data_karyawan as db
import os
def print_menu():

    while True:
        print('''=============Mengubah Data=============
        1.Ubah Data Karyawan
        2.Kembali ke Menu Utama ''')

        UserInput =int(input(f'Silahkan Pilih Sub Menu Data [1-2]: '))
        if UserInput == 1:
            os.system('cls||clear')
            pertanyaan =input('masukan nama karyawan: ')
            flag = False
            for key in range(len(db.data_karyawan)):
                if pertanyaan == db.data_karyawan[key]['namakaryawan']:
                    print(f"{'namakaryawan':<20}|{'umur':<20}|{'jabatan':<20}|{'jeniskelamin':<20}{'gaji':<20}")
                    NAMA = db.data_karyawan[key]['namakaryawan']
                    UMUR = db.data_karyawan[key]['umur']
                    JABATAN= db.data_karyawan[key]['jabatan']
                    JENISKELAMIN= db.data_karyawan[key]['jeniskelamin']
                    GAJI = db.data_karyawan[key]['gaji']
                    flag = True
                    break
            if flag :


                print(f"{NAMA:<20}|{UMUR:<20}|{JABATAN:<20}|{JENISKELAMIN:<20}|{GAJI:<20}")
                user_input = input('data apa yang mau diubah? :')
                if user_input == 'namakaryawan':
                    Data_baru = input('masukan data baru : ')
                    db.data_karyawan[key]['namakaryawan']=Data_baru
                elif user_input == 'umur':
                    Data_baru = input('masukan data baru :')
                    db.data_karyawan[key]['umur']=Data_baru
                elif user_input == 'jabatan':
                    Data_baru = input('masukan data baru :')
                    db.data_karyawan[key]['jabatan']=Data_baru
                elif user_input == 'jeniskelamin':
                    Data_baru = input('masukan data baru :')
                    db.data_karyawan[key]['jeniskelamin']=Data_baru
                elif user_input == 'gaji':
                    Data_baru = input('masukan data baru :')
                    db.data_karyawan[key]['gaji']=Data_baru
            else :
                print('data tidak ditemukan .')

        elif UserInput == 2:
            os.system('cls||clear')
            break
