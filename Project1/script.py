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
    if not os.path.exists(BACKUP_FOLDER):
        os.mkdir(BACKUP_FOLDER)
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H")
    backUp_path = os.path.join(BACKUP_FOLDER, f"backup_{timestamp}")

    try:
        shutil.copytree(SOURCE_FOLDER, backUp_path)
        logging.info(f"Backup created: {backUp_path}")
        print(f"Backup created: {backUp_path}")
    except:
        logging.warning(f"Skipping invalid folder: {backUp_path}")
        print(f"Skipping Backup folder already exist: {backUp_path}")

## Function to remove old backups...
def deleteOldBackup():
    for folder in os.listdir(BACKUP_FOLDER):
        folder_path = os.path.join(BACKUP_FOLDER, folder)
        if os.path.isdir(folder_path):
            timestamp = folder.replace("backup_", "")
            folder_time = datetime.datetime.strptime(timestamp, "%Y-%m-%d_%H")
            age = (datetime.datetime.now() - folder_time).days
            if age > RETENTION_TIME:
                shutil.rmtree(folder_path)
                logging.info("Old Bakup folder deleted.")
                print("Old Bakup folder deleted.")


## Run The Functions...
if __name__ == "__main__":
    create_backup()
    deleteOldBackup()