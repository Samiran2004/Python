import kagglehub
import os

def download_dataset_from_kaggle(dataset_name, folder_name="./data"):
    os.makedirs(folder_name, exist_ok=True)
    print("Folder created...")
    try:
        os.environ['KAGGLEHUB_CACHE'] = f"./{folder_name}"
        print("Downloading dataset...")
        path = kagglehub.dataset_download(dataset_name)
        print("Dataset downloaded...")
        print(path)
    except Exception as e:
        print(f"Error: {e}")

download_dataset_from_kaggle(dataset_name="burak3ergun/loan-data-set")