import kagglehub
import os

def download_kaggle_dataset(filename, foldername="./data"):
    print("Creating folder...")
    os.makedirs(foldername, exist_ok=True)
    print(f"Folder created {foldername}")

    try:
        print("Importing dataset...")
        os.environ['KAGGLEHUB_CACHE'] = f"./{foldername}"

        path = kagglehub.dataset_download(filename)

        print(f"Dataset downloaded successfully...")
        print(f"Location: {path}")
    except Exception as e:
        print(f"Error: {e}")


download_kaggle_dataset(filename="sudarshan24byte/online-food-dataset")