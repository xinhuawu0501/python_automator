import os
import shutil

def group_by_file_type(path: str):
    groups = {}

    for d in os.listdir(path):
        full_path = os.path.join(path, d)

        if os.path.isdir(full_path):
            continue

        filename, file_extension = os.path.splitext(full_path)

        if not groups.get(file_extension):
            groups[file_extension] = []

        groups[file_extension].append(d)
    
    return groups


def move_file_in_os(path, groups):
    for file_ext, files in groups.items():
        file_type = file_ext.replace('.', '').upper()
        new_folder = os.path.join(path, file_type)

        os.makedirs(new_folder, exist_ok=True)

        for f in files:
            shutil.move(os.path.join(path, f), os.path.join(new_folder, f))

if __name__ == '__main__':
    path_to_clean = ''
    while True:
        path_to_clean = input("Type in the folder path you want to clean\n") 
        if os.path.isdir(path_to_clean):
            break
        else:
            print("Invalid path. Please try again.")
            
    move_file_in_os(path_to_clean, group_by_file_type(path_to_clean))


    