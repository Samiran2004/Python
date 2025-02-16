import os
import datetime
import logging
import json
import shutil

## Setup logging...
logging.basicConfig(filename="logs/backup.log", level=logging.INFO, format="%(asctime)s - %(message)s")

## Load config file...
with open("configs.json", "r") as config_file:
    config = json.load(config_file)

SOURCE_FOLDER = config["source_folder"]
BACKUP_FOLDER = config["backup_folder"]
RETENTION_TIME = config["retention_time"]

## Function to create backup...
def create_backup():
    # If BACKUP_FOLDER is not exist, then create using os.mkdir()
    if not os.path.exists(BACKUP_FOLDER):
        os.mkdir(BACKUP_FOLDER)
    
    # Create a timestamp using datetime and format it like:-> 2025-02-17_08
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H")
    # Create a backup folder path like:-> backup/backup_2025-02-17_08
    backUp_path = os.path.join(BACKUP_FOLDER, f"backup_{timestamp}")

    # Error handling using try-except
    try:
        #Copy the source files into backup folder...
        shutil.copytree(SOURCE_FOLDER, backUp_path) # use copytree because in the source path there is not only one file exist
        logging.info(f"Backup created: {backUp_path}") # Write the loginfo into log file...
        print(f"Backup created: {backUp_path}")
    # If any error occures
    except:
        logging.warning(f"Skipping invalid folder: {backUp_path}")
        print(f"Skipping Backup folder already exist: {backUp_path}")

## Function to remove old backups...
def deleteOldBackup():
    # Error handling using try-except
    try:
        # All files and folders in backup folder
        for folder in os.listdir(BACKUP_FOLDER):
            # Create a folder path like:-> backup/backup_2025-02-17_08
            folder_path = os.path.join(BACKUP_FOLDER, folder)
            # Check folder path is not a file, Only delete directories
            if os.path.isdir(folder_path):
                # Extract time part from the folder_path: backup_2025-02-17_08 -> 2025-02-17_08
                timestamp = folder.replace("backup_", "")
                folder_time = datetime.datetime.strptime(timestamp, "%Y-%m-%d_%H")
                age = (datetime.datetime.now() - folder_time).days
                # Delete the folder if the folder is older than RETENTION_TIME
                if age > RETENTION_TIME:
                    shutil.rmtree(folder_path)
                    logging.info("Old Bakup folder deleted.")
                    print("Old Bakup folder deleted.")
    # If any error occures
    except:
        logging.error("Error to delete backup folder")
        print("Error to delete backup folder")

## Run The Functions...
if __name__ == "__main__":
    create_backup()
    deleteOldBackup()