import os

main_folder = 'PersianFace'

for folder_name in os.listdir(main_folder):
    folder_path = os.path.join(main_folder, folder_name)

    if os.path.isdir(folder_path):
        for idx, file_name in enumerate(os.listdir(folder_path), start=1):
            file_path = os.path.join(folder_path, file_name)

            file_extension = os.path.splitext(file_name)[1]

            new_file_name = f"{folder_name}_{idx}{file_extension}"
            new_file_path = os.path.join(folder_path, new_file_name)

            os.rename(file_path, new_file_path)

print("all image renamed")
