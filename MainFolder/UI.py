# Программа должна уметь создавать
# заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку.
import Model as m
import sys

def import_p():
    print("Введите текст заметки")
    m._addTele()

def export_p_txt():
    print("Создать заметку")
    m._Create()

def readFile():
    m._readFile_s()

def menu():
    print("выберете из пункта меню \n"
          "1. Внесение данных \n"
          "2. Создание новой заметки \n"
          "3. Просмотр заметки\n"
          "4. Просмотр списка заметок\n"
          "5. Удалить заметку\n"
          "6. Выход"
          )

    x = int(input())
    if x == 1:
       import_p()
       exit()
    elif x == 2:
       export_p_txt()
       exit()
    elif x == 3:
       readFile()
    elif x == 4:
       m.Preview()
    elif x == 5:
       m.DeleteFile()
       exit()
    elif x == 6:
       m.Exit()
    else:
        print("Неверно введены даные")
    menu()
