import os
import kagglehub

def download_kaggle_dataset(dataset_name, folder_name='./data'):
    try:
    #     Create folder...
        os.makedirs(folder_name, exist_ok=True)
        print("Folder created...")
        try:
            os.environ['KAGGLEHUB_CACHE'] = f"./{folder_name}"

            print("Downloading dataset...")
            path = kagglehub.dataset_download(dataset_name)
            print("Dataset downloaded successfully...")
            print(f"Location: {path}")
            print(f"Files: {os.listdir(path=path)}")
        except Exception as e:
            print(f"Error: {e}")
            return None
    except Exception as e:
        print(f"Error: {e}")

download_kaggle_dataset("tawfikelmetwally/employee-dataset")