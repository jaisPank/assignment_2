import os
import shutil

def organize_files(directory):
    
    files = os.listdir(directory)

    
    file_dict = {}

    # Organize files based on their extensions
    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension not in file_dict:
                file_dict[file_extension] = []
            file_dict[file_extension].append(file)

    
    total_files_moved = 0
    for ext, file_list in file_dict.items():
        folder_path = os.path.join(directory, ext[1:])
        os.makedirs(folder_path, exist_ok=True)
        for file in file_list:
            src_path = os.path.join(directory, file)
            dest_path = os.path.join(folder_path, file)
            shutil.move(src_path, dest_path)
            total_files_moved += 1

    return total_files_moved

if __name__ == "__main__":
    directory_path = "/home/shtlp_0031/my_learning/assignment_2/answer2"  
    total_files_moved = organize_files(directory_path)
    print(f"Total number of files moved: {total_files_moved}")

