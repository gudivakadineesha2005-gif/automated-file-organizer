import os
import shutil
#INTERNID: CITS1188
#CodTECH Python Task 1 - Automated File Oraganizer
def organize_files(folder_path):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Music': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.rar', '.7z'],
        'Code': ['.py', '.js', '.html', '.css', '.java']
    }
 print(f"Scanning folder: {folder_path}")
if not os.path.exists(folder_path):
        print("Error: Folder path does not exist!")
        return
for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(folder_path, folder)
                    if not os.path.exists(dest_folder):
                        os.makedirs(dest_folder)
                        print(f"Created folder: {folder}")
                    try:
                        shutil.move(file_path, os.path.join(dest_folder, filename))
                        print(f"Moved: {filename} -> {folder}")
                    except Exception as e:
                        print(f"Error moving {filename}: {e}")
                    break
if __name__ == "__main__":
    print("=== AUTOMATED FILE ORGANIZER ===")
    print("INTERNID: CITS1188")
    target_folder = input("Enter full folder path to organize: ")
    organize_files(target_folder)
    print("\nOrganizing complete!")
