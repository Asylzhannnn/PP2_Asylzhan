#exercise 1

import os  

def list_contents(path):
    if not os.path.exists(path):  
        print("Did not found")
        return

    print("\n Directories:")
    print("\n".join(entry.name for entry in os.scandir(path) if entry.is_dir()) or "Нет директорий")

    print("\n Fils:")
    print("\n".join(entry.name for entry in os.scandir(path) if entry.is_file()) or "Нет файлов")

    print("\n  Files and folder:")
    print("\n".join(entry.name for entry in os.scandir(path)) or "Пустая директория")

# Ввод пути
directory = input("Write road to directory: ")
list_contents(directory)


#exercise 2

import os  #os.access() helps to check and get access for fails and directories

def check_path_access(path):  
    print(f"Проверка доступа к: {path}")
    if os.path.exists(path):    #checks is it exists or not?
        print("Path exists")
    else:
        print("Path does not exist")
        return
    if os.access(path, os.R_OK):   #Читаемыйлифайл (R_OK = Read OK)
        print("Readable")
    else:
        print("Unreadable")
    if os.access(path, os.W_OK):   #можно ли написать(W_OK = Write OK)
        print("Writeable")
    else:
        print("Unwriteable")
    if os.access(path, os.X_OK):   #можно ли запускать(X_OK = Execute OK)
        print("Executable")
    else:
        print("Not executable")
path = input("Write your road to path: ")
check_path_access(path)


#exercise 3

import os  

def check_path(path):
    if os.path.exists(path):  # checking is path exists or not
        print("Path exists")
        print("Directory:", os.path.dirname(path))  # Папка, где находится файл
        print("File name:", os.path.basename(path))  # file itself
    else:
        print("Does not exist")
path = input("Write path to file: ")
check_path(path)


#exercise 4

def count_lines(filename):   #
    with open(filename, "r") as f: 
        return len(f.readlines())  # f.readlines() читает весь файл в список строк
filename = input("File name: ")    #len() считает количество элементов в списке
print("Number of in file:", count_lines(filename))

#exercise 5

def write_listtofile(filename, my_list):
    with open(filename, "w") as f:  # Открываем файл в режиме записи
        f.writelines("\n".join(my_list))  # Записываем список построчно и сразу
my_list = ["Apple", "Banana", "Cherry", "Orange"]
write_listtofile("fruits.txt", my_list)
print("List is written to file")

#exercise 6

import string  

def create_text_files():
    for letter in string.ascii_uppercase:  # Генерируем буквы ABCDEF...-Z
        filename = f"{letter}.txt" #ABCDEF..-Z.txt
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"This is file {filename}\n")  # Записываем текст в файл
create_text_files()

#exercise 7

def copy_file(source, destination):
    with open(source, "r", encoding="utf-8") as src:  # Открываем исходный файл на чтение
        content = src.read()  # Читаем содержимое 
    with open(destination, "w", encoding="utf-8") as dest:  # Открываем целевой файл на запись
        dest.write(content)  # Записываем содержимое
source_file = input("Введите имя исходного файла: ")
destination_file = input("Введите имя файла для копии: ")
copy_file(source_file, destination_file)


#exercise 8

import os  

def delete_file(filepath):
    if not os.path.exists(filepath):  # Проверяем существует ли файл
        print("File is not found")
        return
    if not os.access(filepath, os.W_OK):  #Проверяv можно ли удалить файл (W_OK = write access)
        print("Do not have access for deleting")
        return
    os.remove(filepath)  # Удаляем файл
    print(f"✅ Файл '{filepath}' успешно удалён!")
file_to_delete = input("Введите путь к файлу для удаления: ")
delete_file(file_to_delete)
