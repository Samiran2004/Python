import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found."
    except PermissionError:
        return None, "Permission denied."

def main():
    folders_paths = input("Enter folders name: ").split()

    for folder_path in folders_paths:
        files, errorMessage = list_files_in_folder(folder_path)

        if(files):
            print(f"Files in {folder_path}")
            for file in files:
                print(file)

        else:
            print(f"Error in {folder_path}: {errorMessage}")
    

if __name__ == "__main__":
    main()