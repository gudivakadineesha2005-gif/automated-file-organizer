import os
import shutil
def organize_files(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    for file in files:
        file_extension = os.path.splitext(file)[1][1:].lower()
        if not file_extension:
            continue
            extension_folder = os.path.join(folder_path, file_extension.upper() + "_Files")
        if not os.path.exists(extension_folder):
            os.makedirs(extension_folder)
            print(f"Created folder: {extension_folder}")
        source = os.path.join(folder_path, file)
        destination = os.path.join(extension_folder, file)
        shutil.move(source, destination)
        print(f"Moved: {file} -> {extension_folder}")
    print("\nFile organization completed!")
  if __name__ == "__main__":
    folder_to_organize = input("Enter the full path of folder to organize: ")
    if os.path.exists(folder_to_organize):
        organize_files(folder_to_organize)
    else:
        print("Error: Folder path does not exist!")
