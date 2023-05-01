import PreModel as pm
import UI
import os


def _readFile():
    with open(pm.s) as f:
        list1 = f.readlines()

def _readFile_s():
    with open(pm.s) as f:
        list1 = f.readlines()
        print(*list1)

def _Create():
    with open(pm.s, "w") as f:
        list1 = f.writelines(" ")

def _SaveTXT():
    with open(pm.s, "w") as f:
        f.writelines(_readFile())
        list1 = f.writelines(" ")


def _addTele():
    with open(pm.s, "a+") as f:
        list1 = f.writelines(input()+"\n")

def Preview():
    print(os.listdir())


def DeleteFile():
    if os.path.isfile(pm.s):
        os.remove(pm.s)
        print("success")
    else:
        print("File doesn't exists!")


def Exit():
    print("Вы действительно хотите выйти? Да/Нет" )
    x = input()
    if x == "Да":
        exit()
    elif x == "Нет":
        UI.menu()
    else:
        print("Вы ввели не верные данные попробуйте еще раз")
        Exit()

