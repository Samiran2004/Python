import kagglehub
import os
import shutil

def download_kaggle_dataset(dataset_name, folder_name="data"):

    """Download Kaggle dataset using kagglehub"""

    # Create target folder
    os.makedirs(folder_name, exist_ok=True)
    print(f"Created folder: {folder_name}")

    try:
        os.environ['KAGGLEHUB_CACHE'] = f"./{folder_name}"

        # Downloading dataset...
        print(f"Downloading dataset: {dataset_name}")
        path = kagglehub.dataset_download(dataset_name)

        print(f"Dataset downloaded successfully...")
        print(f"Location: {path}")
        print(f"Files: {os.listdir(path=path)}")
    except Exception as e:
        print(f"Exception: {e}")
        return None
    
download_kaggle_dataset("rishikeshkonapure/hr-analytics-prediction")