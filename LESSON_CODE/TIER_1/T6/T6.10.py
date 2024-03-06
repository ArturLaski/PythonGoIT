import shutil
import os

def create_backup(path, file_name, employee_residence):
    file_path =  path + '/' + file_name
    with open(file_path, 'wb') as fil:
        for k, v in employee_residence.items():
            line = f"{k} {v}\n"
            fil.write(line.encode())

    archive_name = 'backup_folder'
    archive_path = path + '/' + archive_name + ".zip"
    shutil.make_archive(archive_name, 'zip', path)
    return archive_path
