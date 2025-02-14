## Importing the os module...
import os

## Getting Current Working Directory...
print(f"Current Directory: {os.getcwd()}")

## Listing Files & Directories
print(f"Files and Directories: {os.listdir()}")  #Returns a list of all files and directories in the current working directory.

## Creating a New Directory
if os.path.exists("new_folder"):
    print("Folder already exist...")
    os.rmdir("new_folder")
    print("Folder deleted...")
else:
    os.mkdir("new_folder")
    print("Directory created...")

## Creating Nested Directories
os.makedirs("parent_folder/child_folder")
print("Nested Directories Created!")

os.system("ls -l")
os.system("pwd")