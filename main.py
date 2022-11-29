import menus.menu1
import menus.menu2
import menus.menu3
import menus.menu4
import menus.MenuUtama
import os

def start():
    while True:  #Digunakan untukk menjalankan loopingan tersebut sampai hasilnya false
        os.system('cls||clear') 
        input1 = menus.MenuUtama.print_menu()

        if input1 == 1 :
            os.system('cls||clear')
            menus.menu1.print_menu()
        elif input1 == 2:
            os.system('cls||clear')
            menus.menu2.print_menu()
        elif input1 == 3:
            os.system('cls||clear')
            menus.menu3.print_menu()
        elif input1 == 4:
            os.system('cls||clear')
            menus.menu4.print_menu()
        elif input1 == 5:
            break
        else:
            print('input yang anda masukan salah')
            continue

start()
