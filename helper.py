import os
import shutil


address = input("enter the path of the directory")
extension_list = [
    (('png', 'jpg', 'jpeg'), 'Images'),
    (('.csv', '.xls', '.XLS', '.xlsx','.ods'), 'spreadsheet'),
    (('.exe', '.rar', '.zip'), 'zip ')
]

def directory_builder(address):
    for _, dir_name in extension_list:
        if dir_name not in os.listdir(address):
            os.mkdir(address + "\\" +dir_name)

def organizer(address):
    for each_file in os.listdir(address):
        if os.path.isfile(address + "\\" + each_file):
            copy_path = address + "\\" + each_file
            for extension, folder in extension_list:
                if extension is None or each_file.endswith(extension):
                    dest_path = os.path.join(address, folder, each_file)
                    shutil.move(copy_path, dest_path)
                    break


directory_builder(address)
organizer(address)