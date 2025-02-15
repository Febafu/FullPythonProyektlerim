import os
import shutil

EXTENSIONS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css']
}

def create_folders(base_path):
    for category in EXTENSIONS.keys():
        folder_path = os.path.join(base_path, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def organize_files(base_path):
    for file in os.listdir(base_path):
        file_path = os.path.join(base_path, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            for category, extensions in EXTENSIONS.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(base_path, category, file))
                    break

def main():
    base_path = input("Enter the directory to organize: ").strip()
    if os.path.exists(base_path):
        create_folders(base_path)
        organize_files(base_path)
        print("Files have been organized successfully!")
    else:
        print("Invalid directory path!")

if __name__ == "__main__":
    main()
